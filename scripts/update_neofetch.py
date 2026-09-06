#!/usr/bin/env python3
"""Sync profile banner SVGs + snapshot from the full GitHub account database."""

from __future__ import annotations

import json
import math
import os
import re
import sys
from calendar import monthrange
from collections import Counter
from datetime import date, datetime, timedelta, timezone
from json import JSONDecoder
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
SVG_PATHS = [
    ROOT / "neofetch.svg",
    ROOT / "banner-dark.svg",
    ROOT / "banner-light.svg",
]
TRAJECTORY_PATHS = [
    ROOT / "trajectory-dark.svg",
    ROOT / "trajectory-light.svg",
]
SNAPSHOT_PATH = ROOT / "data" / "github-snapshot.json"
WBM_SNAPSHOT_PATH = ROOT / "data" / "whoburnedmore-snapshot.json"
README_PATH = ROOT / "README.md"
USER = os.environ.get("USER_NAME", "mangeshraut712")
TOKEN = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
WBM_HANDLE = os.environ.get("WBM_HANDLE", "mrcommando712")

ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

# Prefer real GitHub primary languages; skip junk labels.
LANG_SKIP = {"None", "HTML", "CSS", "Jupyter Notebook", "TSQL", "MATLAB"}

# Verified across owned repos (package.json / requirements inventory, Jul 2026).
FOCUS_AI = "WebRTC VAD · RAG/BM25 · MCP · PyTorch"
FOCUS_STACK = "Next.js 16 · React 19 · FastAPI · Turbopack"
ROLE = "Applied AI Engineer"
STACK_ICONS = (
    "ts,js,py,swift,react,nextjs,tailwind,fastapi,express,"
    "postgres,supabase,mongodb,docker,vercel,pytorch"
)
STACK_LABEL = (
    "TypeScript · Python · JavaScript · Swift · Next.js 15/16 · React 19 · "
    "FastAPI · Turbopack · PyTorch · WebRTC VAD · BM25 · MCP · Sarvam · "
    "Postgres · Docker · Vercel · GitHub Actions"
)


def gql(query: str, variables: dict | None = None) -> dict:
    if not TOKEN:
        raise SystemExit("ACCESS_TOKEN or GITHUB_TOKEN is required")
    res = requests.post(
        "https://api.github.com/graphql",
        json={"query": query, "variables": variables or {}},
        headers={"Authorization": f"bearer {TOKEN}"},
        timeout=60,
    )
    res.raise_for_status()
    payload = res.json()
    if "errors" in payload:
        raise RuntimeError(payload["errors"])
    return payload["data"]


def age_string(start: date, end: date) -> str:
    y = end.year - start.year
    m = end.month - start.month
    d = end.day - start.day
    if d < 0:
        m -= 1
        prev = end.month - 1 or 12
        year = end.year if end.month > 1 else end.year - 1
        d += monthrange(year, prev)[1]
    if m < 0:
        y -= 1
        m += 12
    return f"{y} years, {m} months, {d} days"


def fmt(n: int) -> str:
    return f"{n:,}"


def fmt_tokens(n: float | int) -> str:
    """Compact token counts: 13.51B / 486.2M / 12.4K."""
    value = float(n)
    abs_value = abs(value)
    if abs_value >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"
    if abs_value >= 1_000_000:
        compact = f"{value / 1_000_000:.1f}"
        if compact.endswith(".0"):
            compact = compact[:-2]
        return f"{compact}M"
    if abs_value >= 1_000:
        compact = f"{value / 1_000:.1f}"
        if compact.endswith(".0"):
            compact = compact[:-2]
        return f"{compact}K"
    return str(int(round(value)))


def fmt_money(n: float | int) -> str:
    return f"${round(float(n)):,}"


def _unescape_next_payload(raw: str) -> str:
    try:
        return json.loads(f'"{raw}"')
    except json.JSONDecodeError:
        return bytes(raw, "utf-8").decode("unicode_escape")


def _iter_next_payloads(html: str) -> list[str]:
    payloads: list[str] = []
    for match in re.finditer(r'self\.__next_f\.push\(\[1,"((?:\\.|[^"\\])*)"\]\)', html):
        payloads.append(_unescape_next_payload(match.group(1)))
    return payloads


def _parse_user_from_text(text: str, handle: str) -> dict | None:
    marker = f'"handle":"{handle}"'
    start = 0
    decoder = JSONDecoder()
    while True:
        idx = text.find(marker, start)
        if idx < 0:
            break
        window = text[idx : idx + 4000]
        if '"allTimeRank"' not in window and '"rank"' not in window:
            start = idx + len(marker)
            continue
        rank_m = re.search(
            r'"rank":(\d+),"dailyRank":(\d+),"weeklyRank":(\d+),"allTimeRank":(\d+)',
            window,
        )
        totals_m = re.search(r'"totals":(\{[^}]+\})', window)
        daily_idx = text.find('"daily":', idx)
        if not rank_m or not totals_m or daily_idx < 0:
            start = idx + len(marker)
            continue
        try:
            daily, _ = decoder.raw_decode(text[daily_idx + len('"daily":') :])
            totals = json.loads(totals_m.group(1))
        except (json.JSONDecodeError, ValueError):
            start = idx + len(marker)
            continue
        if not isinstance(daily, list):
            start = idx + len(marker)
            continue
        return {
            "handle": handle,
            "rank": int(rank_m.group(1)),
            "dailyRank": int(rank_m.group(2)),
            "weeklyRank": int(rank_m.group(3)),
            "allTimeRank": int(rank_m.group(4)),
            "totals": totals,
            "daily": daily,
        }
    return None


def _parse_total_users(html: str, rank: int) -> int | None:
    match = re.search(rf"#{rank}\s+of\s+(\d+)", html)
    if match:
        return int(match.group(1))
    match = re.search(r"#\d+\s+of\s+(\d+)", html)
    if match:
        return int(match.group(1))
    return None


def _sum_period(daily: list[dict], start: date, end: date) -> tuple[float, float]:
    tokens = 0.0
    cost = 0.0
    for row in daily:
        try:
            day = date.fromisoformat(str(row["date"])[:10])
        except (KeyError, TypeError, ValueError):
            continue
        if start <= day <= end:
            tokens += float(row.get("tokens") or 0)
            cost += float(row.get("costUSD") or 0)
    return tokens, cost


def fetch_whoburnedmore(handle: str = WBM_HANDLE) -> dict:
    """Scrape public WhoBurnedMore profile HTML (Next.js flight payload)."""
    res = requests.get(
        f"https://whoburnedmore.com/u/{handle}",
        headers={
            "User-Agent": "mangeshraut712-neofetch-bot/1.0 (+https://github.com/mangeshraut712/mangeshraut712)",
            "Accept": "text/html,application/xhtml+xml",
        },
        timeout=60,
    )
    res.raise_for_status()
    html = res.text

    record = _parse_user_from_text(html, handle)
    if record is None:
        for payload in _iter_next_payloads(html):
            record = _parse_user_from_text(payload, handle)
            if record is not None:
                break
    if record is None:
        raise RuntimeError(f"Could not parse WhoBurnedMore payload for {handle}")

    totals = record["totals"]
    daily = record["daily"]
    rank = int(record["allTimeRank"] or record["rank"])
    total_users = _parse_total_users(html, rank)
    if total_users is None:
        total_users = _parse_total_users("".join(_iter_next_payloads(html)), rank)

    today = datetime.now(timezone.utc).date()
    week_start = today - timedelta(days=today.weekday())
    today_tokens, today_cost = _sum_period(daily, today, today)
    week_tokens, week_cost = _sum_period(daily, week_start, today)

    percentile = None
    if total_users and total_users > 0:
        percentile = math.ceil(rank / total_users * 100)

    if total_users and percentile is not None:
        rank_line = f"#{rank} of {total_users} (top {percentile}%)"
    else:
        rank_line = f"#{rank}"

    lifetime_tokens = float(totals.get("tokens") or 0)
    lifetime_cost = float(totals.get("costUSD") or 0)
    active_days = int(totals.get("days") or 0)
    streak_days = int(totals.get("streakDays") or 0)

    lifetime_line = (
        f"{fmt_tokens(lifetime_tokens)} tokens · {fmt_money(lifetime_cost)} · "
        f"{active_days} active days · {streak_days}d streak"
    )
    today_line = f"{fmt_tokens(today_tokens)} · {fmt_money(today_cost)}"
    week_line = f"{fmt_tokens(week_tokens)} · {fmt_money(week_cost)}"

    return {
        "handle": handle,
        "url": f"https://whoburnedmore.com/u/{handle}",
        "rank": rank,
        "daily_rank": int(record["dailyRank"]),
        "weekly_rank": int(record["weeklyRank"]),
        "all_time_rank": int(record["allTimeRank"]),
        "total_users": total_users,
        "top_percentile": percentile,
        "lifetime_tokens": lifetime_tokens,
        "lifetime_cost_usd": lifetime_cost,
        "active_days": active_days,
        "streak_days": streak_days,
        "longest_streak_days": int(totals.get("longestStreakDays") or 0),
        "today_tokens": today_tokens,
        "today_cost_usd": today_cost,
        "week_tokens": week_tokens,
        "week_cost_usd": week_cost,
        "week_start": week_start.isoformat(),
        "as_of": today.isoformat(),
        "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "WhoBurnedMore public profile HTML (Next.js payload)",
        "burn_rank_data": rank_line,
        "burn_lifetime_data": lifetime_line,
        "burn_today_data": today_line,
        "burn_week_data": week_line,
    }


def write_whoburnedmore_snapshot(burn: dict) -> None:
    WBM_SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {k: v for k, v in burn.items() if not k.startswith("burn_")}
    WBM_SNAPSHOT_PATH.write_text(json.dumps(payload, indent=2) + "\n")


def bump_banner_cache_buster(stamp: str) -> None:
    """Force GitHub/raw CDN to refetch banner/neofetch SVGs after each daily sync."""
    if not README_PATH.exists():
        return
    text = README_PATH.read_text()
    text = re.sub(
        r"(banner-(?:dark|light)\.svg|neofetch\.svg)\?v=[^\"\s]+",
        rf"\1?v={stamp}",
        text,
    )
    README_PATH.write_text(text)


def update_readme_whoburnedmore(burn: dict) -> None:
    if not README_PATH.exists():
        return
    stamp = datetime.now(timezone.utc).strftime("%Y%m%d")
    block = f"""<!-- whoburnedmore:start -->
<p align="center">
  <sup>
    <a href="{burn['url']}">WhoBurnedMore @{burn['handle']}</a>
    · Rank {burn['burn_rank_data']}
    · Lifetime {burn['burn_lifetime_data']}
    · Today {burn['burn_today_data']}
    · This week {burn['burn_week_data']}
  </sup>
</p>
<!-- whoburnedmore:end -->"""
    text = README_PATH.read_text()
    text, n = re.subn(
        r"<!-- whoburnedmore:start -->[\s\S]*?<!-- whoburnedmore:end -->",
        block,
        text,
        count=1,
    )
    if n:
        README_PATH.write_text(text)
    bump_banner_cache_buster(stamp)


def fetch_owned_repos() -> list[dict]:
    """Page through every owned repository (full account inventory)."""
    nodes: list[dict] = []
    cursor = None
    while True:
        data = gql(
            """
            query($login: String!, $after: String) {
              user(login: $login) {
                repositories(
                  first: 100
                  after: $after
                  ownerAffiliations: OWNER
                  orderBy: { field: UPDATED_AT, direction: DESC }
                ) {
                  pageInfo { hasNextPage endCursor }
                  nodes {
                    name
                    isFork
                    isPrivate
                    stargazerCount
                    forkCount
                    primaryLanguage { name }
                    homepageUrl
                    description
                    pushedAt
                  }
                }
              }
            }
            """,
            {"login": USER, "after": cursor},
        )
        conn = data["user"]["repositories"]
        nodes.extend(conn["nodes"])
        if not conn["pageInfo"]["hasNextPage"]:
            break
        cursor = conn["pageInfo"]["endCursor"]
    return nodes


def year_window(year: int, today: date) -> tuple[str, str]:
    start = f"{year}-01-01T00:00:00Z"
    if year < today.year:
        end = f"{year}-12-31T23:59:59Z"
    else:
        end = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    return start, end


def fetch_stats() -> dict:
    today = date.today()
    year = today.year

    profile = gql(
        """
        query($login: String!) {
          user(login: $login) {
            createdAt
            bio
            location
            followers { totalCount }
            following { totalCount }
            repositoriesContributedTo(
              first: 1
              contributionTypes: [COMMIT, ISSUE, PULL_REQUEST, REPOSITORY]
            ) { totalCount }
          }
        }
        """,
        {"login": USER},
    )["user"]

    created = date.fromisoformat(profile["createdAt"][:10])
    repos = fetch_owned_repos()
    owned = [r for r in repos if not r["isFork"]]
    stars = sum(r["stargazerCount"] for r in owned)
    forks = sum(r["forkCount"] for r in owned)
    lang_counts = Counter(
        (r["primaryLanguage"] or {}).get("name")
        for r in owned
        if (r["primaryLanguage"] or {}).get("name")
    )
    top_langs = [
        name
        for name, _ in lang_counts.most_common()
        if name not in LANG_SKIP
    ][:4]
    if not top_langs:
        top_langs = [name for name, _ in lang_counts.most_common(4)]

    # YTD calendar + breakdown
    ytd_from, ytd_to = year_window(year, today)
    ytd_block = gql(
        """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            contributionsCollection(from: $from, to: $to) {
              contributionCalendar {
                totalContributions
                weeks { contributionDays { date contributionCount } }
              }
              totalCommitContributions
              totalPullRequestContributions
              totalIssueContributions
              totalPullRequestReviewContributions
              restrictedContributionsCount
            }
          }
        }
        """,
        {"login": USER, "from": ytd_from, "to": ytd_to},
    )["user"]["contributionsCollection"]

    days = [
        day
        for week in ytd_block["contributionCalendar"]["weeks"]
        for day in week["contributionDays"]
    ]
    ytd = ytd_block["contributionCalendar"]["totalContributions"]
    counts = [d["contributionCount"] for d in days]
    best = max(counts) if counts else 0
    best_date = next((d["date"] for d in days if d["contributionCount"] == best), "")
    elapsed = max(1, (today - date(year, 1, 1)).days + 1)
    avg = ytd / elapsed

    longest = current = 0
    for c in counts:
        if c > 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    # All-time contributions: every year since account creation
    yearly: dict[str, int] = {}
    lifetime = 0
    for y in range(created.year, year + 1):
        frm, to = year_window(y, today)
        chunk = gql(
            """
            query($login: String!, $from: DateTime!, $to: DateTime!) {
              user(login: $login) {
                contributionsCollection(from: $from, to: $to) {
                  contributionCalendar { totalContributions }
                }
              }
            }
            """,
            {"login": USER, "from": frm, "to": to},
        )
        n = chunk["user"]["contributionsCollection"]["contributionCalendar"][
            "totalContributions"
        ]
        yearly[str(y)] = n
        lifetime += n

    rest = requests.get(
        f"https://api.github.com/users/{USER}",
        headers={"Authorization": f"bearer {TOKEN}"},
        timeout=30,
    )
    rest.raise_for_status()
    public_repos = rest.json()["public_repos"]

    if best_date:
        parsed = datetime.strptime(best_date, "%Y-%m-%d")
        best_label = f"{parsed.strftime('%b')} {parsed.day}"
    else:
        best_label = "—"

    location = (profile.get("location") or "Pune, MH, India").strip()
    langs_label = " · ".join(top_langs) if top_langs else "—"

    return {
        "lifetime_data": fmt(lifetime),
        "ytd_data": fmt(ytd),
        "repos_data": str(public_repos),
        "stars_data": str(stars),
        "forks_data": str(forks),
        "owned_data": str(len(owned)),
        "prs_data": fmt(ytd_block.get("totalPullRequestContributions", 0)),
        "commits_data": fmt(ytd_block.get("totalCommitContributions", 0)),
        "langs_data": langs_label,
        "role_data": ROLE,
        "focus_ai_data": FOCUS_AI,
        "focus_stack_data": FOCUS_STACK,
        "host_data": location,
        "uptime_data": age_string(created, today),
        "follower_data": str(profile["followers"]["totalCount"]),
        "following_data": str(profile["following"]["totalCount"]),
        "stack_icons": STACK_ICONS,
        "stack_label": STACK_LABEL,
        # raw / snapshot fields
        "owned_raw": len(owned),
        "public_raw": public_repos,
        "stars_raw": stars,
        "forks_raw": forks,
        "followers_raw": profile["followers"]["totalCount"],
        "following_raw": profile["following"]["totalCount"],
        "lifetime_raw": lifetime,
        "ytd_raw": ytd,
        "avg_raw": f"{avg:.2f}",
        "best_raw": best,
        "best_date": best_label,
        "streak_raw": longest,
        "prs_raw": ytd_block.get("totalPullRequestContributions", 0),
        "commits_raw": ytd_block.get("totalCommitContributions", 0),
        "issues_raw": ytd_block.get("totalIssueContributions", 0),
        "reviews_raw": ytd_block.get("totalPullRequestReviewContributions", 0),
        "private_raw": ytd_block.get("restrictedContributionsCount", 0),
        "contributed_to_raw": profile["repositoriesContributedTo"]["totalCount"],
        "languages": dict(lang_counts.most_common()),
        "yearly_contributions": yearly,
        "created_at": profile["createdAt"][:10],
        "location": location,
        "bio": profile.get("bio") or "",
        "year": year,
        "synced_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source": "GitHub GraphQL + REST (full owned-repo inventory + all-year contributions)",
    }


def set_text(root: ET.Element, element_id: str, value: str) -> None:
    for el in root.iter():
        if el.attrib.get("id") == element_id:
            el.text = value
            return


def update_svgs(stats: dict | None = None, burn: dict | None = None) -> None:
    mapping: dict[str, str] = {}
    if stats:
        mapping.update(
            {
                "lifetime_data": stats["lifetime_data"],
                "ytd_data": stats["ytd_data"],
                "repos_data": stats["repos_data"],
                "stars_data": stats["stars_data"],
                "forks_data": stats["forks_data"],
                "owned_data": stats["owned_data"],
                "prs_data": stats["prs_data"],
                "commits_data": stats["commits_data"],
                "langs_data": stats["langs_data"],
                "role_data": stats["role_data"],
                "focus_ai_data": stats["focus_ai_data"],
                "focus_stack_data": stats["focus_stack_data"],
                "host_data": stats["host_data"],
                "follower_data": stats["follower_data"],
                "uptime_data": stats["uptime_data"],
                # light-theme aliases
                "lifetime_data_light": stats["lifetime_data"],
                "ytd_data_light": stats["ytd_data"],
                "repos_data_light": stats["repos_data"],
                "stars_data_light": stats["stars_data"],
                "forks_data_light": stats["forks_data"],
                "owned_data_light": stats["owned_data"],
                "prs_data_light": stats["prs_data"],
                "commits_data_light": stats["commits_data"],
                "langs_data_light": stats["langs_data"],
                "role_data_light": stats["role_data"],
                "focus_ai_data_light": stats["focus_ai_data"],
                "focus_stack_data_light": stats["focus_stack_data"],
                "host_data_light": stats["host_data"],
                "follower_data_light": stats["follower_data"],
                "uptime_data_light": stats["uptime_data"],
            }
        )
    if burn:
        mapping.update(
            {
                "burn_rank_data": burn["burn_rank_data"],
                "burn_lifetime_data": burn["burn_lifetime_data"],
                "burn_today_data": burn["burn_today_data"],
                "burn_week_data": burn["burn_week_data"],
                "burn_rank_data_light": burn["burn_rank_data"],
                "burn_lifetime_data_light": burn["burn_lifetime_data"],
                "burn_today_data_light": burn["burn_today_data"],
                "burn_week_data_light": burn["burn_week_data"],
            }
        )
    for path in SVG_PATHS:
        if not path.exists():
            continue
        tree = ET.parse(path)
        root = tree.getroot()
        for key, value in mapping.items():
            set_text(root, key, value)
        tree.write(path, encoding="utf-8", xml_declaration=True)

    if not stats:
        return
    yearly = stats.get("yearly_contributions") or {}
    traj = {}
    for y, n in yearly.items():
        traj[f"y{y}_count"] = fmt(int(n))
        traj[f"y{y}_count_light"] = fmt(int(n))
    for path in TRAJECTORY_PATHS:
        if not path.exists():
            continue
        tree = ET.parse(path)
        root = tree.getroot()
        for key, value in traj.items():
            set_text(root, key, value)
        tree.write(path, encoding="utf-8", xml_declaration=True)


def write_snapshot(stats: dict) -> None:
    SNAPSHOT_PATH.parent.mkdir(parents=True, exist_ok=True)
    payload = {
        "login": USER,
        "source": stats["source"],
        "synced_at": stats["synced_at"],
        "created_at": stats["created_at"],
        "location": stats["location"],
        "bio": stats["bio"],
        "public_repos": stats["public_raw"],
        "owned_non_fork": stats["owned_raw"],
        "stars_on_owned": stats["stars_raw"],
        "forks_on_owned": stats["forks_raw"],
        "followers": stats["followers_raw"],
        "following": stats["following_raw"],
        "contributed_to_repos": stats["contributed_to_raw"],
        "contributions_all_time": stats["lifetime_raw"],
        "contributions_by_year": stats["yearly_contributions"],
        "ytd": {
            "year": stats["year"],
            "contributions": stats["ytd_raw"],
            "commits": stats["commits_raw"],
            "pull_requests": stats["prs_raw"],
            "issues": stats["issues_raw"],
            "reviews": stats["reviews_raw"],
            "private": stats["private_raw"],
            "avg_per_day": stats["avg_raw"],
            "best_day": stats["best_raw"],
            "best_date": stats["best_date"],
            "longest_streak_days": stats["streak_raw"],
        },
        "primary_languages": stats["languages"],
        "stack": {
            "icons": stats["stack_icons"],
            "label": stats["stack_label"],
            "focus_ai": stats["focus_ai_data"],
            "focus_stack": stats["focus_stack_data"],
            "evidence": {
                "next_js": "15.3–16.1 across flagship apps",
                "react": "18.2 / 19.x across apps",
                "top_deps": [
                    "typescript",
                    "react",
                    "next",
                    "tailwindcss",
                    "fastapi",
                    "pytorch",
                    "express",
                    "supabase",
                ],
            },
        },
    }
    SNAPSHOT_PATH.write_text(json.dumps(payload, indent=2) + "\n")


def update_readme(stats: dict) -> None:
    """Sync stack icons only — stats live in the banner SVG (no README dupes)."""
    if not README_PATH.exists():
        return
    icons = f"""<!-- stack-icons:start -->
  <img src="https://skillicons.dev/icons?i={stats['stack_icons']}" alt="Tech stack from GitHub repos" />
  <!-- stack-icons:end -->"""
    text = README_PATH.read_text()
    # Drop legacy duplicate blocks if present
    text = re.sub(
        r"\n*<!-- github-data:start -->[\s\S]*?<!-- github-data:end -->\n*",
        "\n",
        text,
        count=1,
    )
    text = re.sub(
        r"\n*<p align=\"center\">\s*<sup><!-- stack-label:start -->[\s\S]*?<!-- stack-label:end --></sup>\s*</p>\n*",
        "\n",
        text,
        count=1,
    )
    text, n = re.subn(
        r"<!-- stack-icons:start -->[\s\S]*?<!-- stack-icons:end -->",
        icons,
        text,
        count=1,
    )
    if n:
        README_PATH.write_text(text)


def main() -> int:
    stats = None
    if TOKEN:
        stats = fetch_stats()
        write_snapshot(stats)
        update_readme(stats)
        print("Synced profile from full GitHub account:")
        for k in (
            "public_raw",
            "owned_raw",
            "stars_raw",
            "forks_raw",
            "lifetime_raw",
            "ytd_raw",
            "prs_raw",
            "commits_raw",
            "langs_data",
            "synced_at",
        ):
            print(f"  {k}: {stats[k]}")
    else:
        print("Skipping GitHub GraphQL sync (no ACCESS_TOKEN/GITHUB_TOKEN)")

    burn = fetch_whoburnedmore()
    write_whoburnedmore_snapshot(burn)
    update_readme_whoburnedmore(burn)
    update_svgs(stats, burn)
    print("Synced WhoBurnedMore stats:")
    for k in (
        "handle",
        "burn_rank_data",
        "burn_lifetime_data",
        "burn_today_data",
        "burn_week_data",
        "synced_at",
    ):
        print(f"  {k}: {burn[k]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
