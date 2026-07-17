#!/usr/bin/env python3
"""Sync profile banner SVGs + snapshot from the full GitHub account database."""

from __future__ import annotations

import json
import os
import re
import sys
from calendar import monthrange
from collections import Counter
from datetime import date, datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
SVG_PATHS = [
    ROOT / "neofetch.svg",
    ROOT / "banner-dark.svg",
    ROOT / "banner-light.svg",
]
SNAPSHOT_PATH = ROOT / "data" / "github-snapshot.json"
README_PATH = ROOT / "README.md"
USER = os.environ.get("USER_NAME", "mangeshraut712")
TOKEN = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")

ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")

# Prefer real GitHub primary languages; skip junk labels.
LANG_SKIP = {"None", "HTML", "CSS", "Jupyter Notebook", "TSQL", "MATLAB"}


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
    langs_label = ", ".join(top_langs) if top_langs else "—"

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
        "host_data": location,
        "uptime_data": age_string(created, today),
        "follower_data": str(profile["followers"]["totalCount"]),
        "following_data": str(profile["following"]["totalCount"]),
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


def update_svgs(stats: dict) -> None:
    mapping = {
        "lifetime_data": stats["lifetime_data"],
        "ytd_data": stats["ytd_data"],
        "repos_data": stats["repos_data"],
        "stars_data": stats["stars_data"],
        "forks_data": stats["forks_data"],
        "owned_data": stats["owned_data"],
        "prs_data": stats["prs_data"],
        "commits_data": stats["commits_data"],
        "langs_data": stats["langs_data"],
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
        "host_data_light": stats["host_data"],
        "follower_data_light": stats["follower_data"],
        "uptime_data_light": stats["uptime_data"],
    }
    for path in SVG_PATHS:
        if not path.exists():
            continue
        tree = ET.parse(path)
        root = tree.getroot()
        for key, value in mapping.items():
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
    }
    SNAPSHOT_PATH.write_text(json.dumps(payload, indent=2) + "\n")


def update_readme(stats: dict) -> None:
    """Keep a single auto-synced GitHub source block in the README."""
    if not README_PATH.exists():
        return
    block = f"""<!-- github-data:start -->
<p align="center">
  <sup>Synced from full GitHub account · {stats['synced_at'][:10]}</sup><br/>
  <code>{stats['public_raw']} repos</code>
  · <code>{stats['owned_raw']} owned</code>
  · <code>{stats['stars_raw']} stars</code>
  · <code>{stats['forks_raw']} forks</code>
  · <code>{fmt(stats['lifetime_raw'])} contributions</code>
  · <code>{fmt(stats['ytd_raw'])} in {stats['year']}</code>
  · <code>{stats['prs_raw']} PRs</code>
  · <code>{stats['langs_data']}</code>
</p>
<!-- github-data:end -->"""
    text = README_PATH.read_text()
    pattern = r"<!-- github-data:start -->[\s\S]*?<!-- github-data:end -->"
    if re.search(pattern, text):
        text = re.sub(pattern, block, text, count=1)
    else:
        # Place after hero badges / before Built
        anchor = "\n---\n\n### Built"
        if anchor in text:
            text = text.replace(anchor, "\n\n" + block + "\n\n---\n\n### Built", 1)
        else:
            text = text.rstrip() + "\n\n" + block + "\n"
    README_PATH.write_text(text)


def main() -> int:
    stats = fetch_stats()
    update_svgs(stats)
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
    return 0


if __name__ == "__main__":
    sys.exit(main())
