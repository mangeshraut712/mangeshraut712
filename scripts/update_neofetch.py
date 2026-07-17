#!/usr/bin/env python3
"""Refresh dynamic stats inside neofetch.svg using the GitHub GraphQL API."""

from __future__ import annotations

import os
import re
import sys
from calendar import monthrange
from datetime import date, datetime, timezone
from pathlib import Path
from xml.etree import ElementTree as ET

import requests

ROOT = Path(__file__).resolve().parents[1]
SVG_PATH = ROOT / "neofetch.svg"
README_PATH = ROOT / "README.md"
USER = os.environ.get("USER_NAME", "mangeshraut712")
TOKEN = os.environ.get("ACCESS_TOKEN") or os.environ.get("GITHUB_TOKEN")
ACCOUNT_CREATED = date(2021, 11, 27)

NS = {"svg": "http://www.w3.org/2000/svg"}
ET.register_namespace("", "http://www.w3.org/2000/svg")
ET.register_namespace("xlink", "http://www.w3.org/1999/xlink")


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


def fetch_stats() -> dict:
    today = date.today()
    year = today.year
    data = gql(
        """
        query($login: String!, $from: DateTime!, $to: DateTime!) {
          user(login: $login) {
            followers { totalCount }
            repositories(first: 100, ownerAffiliations: OWNER, isFork: false) {
              totalCount
              nodes { stargazerCount }
            }
            contributionsCollection(from: $from, to: $to) {
              contributionCalendar {
                totalContributions
                weeks { contributionDays { date contributionCount } }
              }
            }
          }
          viewer { repositories(privacy: PUBLIC) { totalCount } }
        }
        """,
        {
            "login": USER,
            "from": f"{year}-01-01T00:00:00Z",
            "to": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        },
    )

    user = data["user"]
    days = [
        day
        for week in user["contributionsCollection"]["contributionCalendar"]["weeks"]
        for day in week["contributionDays"]
    ]
    ytd = user["contributionsCollection"]["contributionCalendar"]["totalContributions"]
    counts = [d["contributionCount"] for d in days]
    best = max(counts) if counts else 0
    best_date = next((d["date"] for d in days if d["contributionCount"] == best), "")
    elapsed = max(1, (today - date(year, 1, 1)).days + 1)
    avg = ytd / elapsed

    # longest streak in YTD window
    longest = current = 0
    for c in counts:
        if c > 0:
            current += 1
            longest = max(longest, current)
        else:
            current = 0

    # lifetime contributions across years since account creation
    lifetime = 0
    for y in range(ACCOUNT_CREATED.year, year + 1):
        start = f"{y}-01-01T00:00:00Z"
        end = f"{y}-12-31T23:59:59Z"
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
            {"login": USER, "from": start, "to": end},
        )
        lifetime += chunk["user"]["contributionsCollection"]["contributionCalendar"][
            "totalContributions"
        ]

    stars = sum(n["stargazerCount"] for n in user["repositories"]["nodes"])
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

    return {
        "uptime_data": age_string(ACCOUNT_CREATED, today),
        "repo_data": str(user["repositories"]["totalCount"]),
        "public_data": str(public_repos),
        "star_data": str(stars),
        "contrib_data": fmt(lifetime),
        "follower_data": str(user["followers"]["totalCount"]),
        "ytd_data": fmt(ytd),
        "avg_data": f"{avg:.2f}/day",
        "streak_data": str(longest),
        "best_data": str(best),
        "best_date": best_label,
        "ytd_raw": ytd,
        "avg_raw": f"{avg:.2f}",
        "best_raw": best,
        "streak_raw": longest,
        "year": year,
    }


def set_text(root: ET.Element, element_id: str, value: str) -> None:
    for el in root.iter():
        if el.attrib.get("id") == element_id:
            el.text = value
            return


def update_svg(stats: dict) -> None:
    tree = ET.parse(SVG_PATH)
    root = tree.getroot()
    for key in (
        "uptime_data",
        "repo_data",
        "public_data",
        "star_data",
        "contrib_data",
        "follower_data",
        "ytd_data",
        "avg_data",
        "streak_data",
        "best_data",
    ):
        set_text(root, key, stats[key])

    set_text(root, "best_note", f" on {stats['best_date']} · open to AI/SaaS roles")
    tree.write(SVG_PATH, encoding="utf-8", xml_declaration=True)


def update_readme_activity(stats: dict) -> None:
    text = README_PATH.read_text()
    table = f"""## {stats['year']} Activity

| Metric | Value |
| --- | --- |
| Contributions (YTD) | **{stats['ytd_data']}** |
| Avg / day | **{stats['avg_raw']}** |
| Best day | **{stats['best_raw']}** ({stats['best_date']}) |
| Longest streak | **{stats['streak_raw']} days** |
"""
    updated, n = re.subn(
        r"## \d{4} Activity\n\n\| Metric \| Value \|[\s\S]*?\| Longest streak \|.*\|\n",
        table + "\n",
        text,
        count=1,
    )
    if n:
        README_PATH.write_text(updated)


def main() -> int:
    stats = fetch_stats()
    update_svg(stats)
    update_readme_activity(stats)
    print("Updated neofetch.svg and README activity table:")
    for k, v in stats.items():
        print(f"  {k}: {v}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
