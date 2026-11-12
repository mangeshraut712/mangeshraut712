"""Keep the dated OSS evidence, README counts and featured cases consistent."""

from collections import Counter
import json
from pathlib import Path
import re
import unittest


ROOT = Path(__file__).resolve().parents[1]


class OssScoreboardTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "data/oss-scoreboard.json").read_text())
        cls.readme = (ROOT / "README.md").read_text()

    def test_all_records_are_unique_authored_merges(self):
        records = self.data["merge_evidence"]
        self.assertEqual(len(records), self.data["total"])
        self.assertEqual(len({record["id"] for record in records}), len(records))
        self.assertEqual(len({record["url"] for record in records}), len(records))
        for record in records:
            self.assertEqual(record["author"], "mangeshraut712")
            self.assertIs(record["merged"], True)
            self.assertRegex(record["merged_at"], r"^\d{4}-\d{2}-\d{2}T.+Z$")
            self.assertEqual(
                record["url"],
                f'https://github.com/{record["repo"]}/pull/{record["number"]}',
            )

    def test_owner_counts_and_urls_match_merge_evidence(self):
        records = self.data["merge_evidence"]
        owners = [group["owner"] for group in self.data["organizations"]]
        self.assertEqual(len(owners), len(set(owners)))
        self.assertEqual(set(owners), {record["owner"] for record in records})
        self.assertEqual(sum(group["count"] for group in self.data["organizations"]), self.data["total"])
        for group in self.data["organizations"]:
            expected = {record["url"] for record in records if record["owner"] == group["owner"]}
            self.assertEqual(set(group["prs"]), expected)
            self.assertEqual(group["count"], len(group["prs"]))
            self.assertEqual(group["count"], len(expected))
            self.assertTrue(all(record["company"] == group["company"] for record in records if record["owner"] == group["owner"]))

    def test_readme_company_table_matches_snapshot(self):
        section = self.readme.split("#### By company group", 1)[1].split("#### Selected Engineering Impact", 1)[0]
        rows = dict(re.findall(r"^\| \[([^]]+)\]\([^)]+\) \| (\d+) \|", section, re.MULTILINE))
        expected = Counter(record["company"] for record in self.data["merge_evidence"])
        self.assertEqual({name: int(count) for name, count in rows.items()}, dict(expected))

    def test_readme_goal_matches_snapshot(self):
        total, goal = self.data["total"], self.data["goal"]
        self.assertIn(f"{total} / {goal}", self.readme)
        self.assertIn(f"**{total} merged pull requests**", self.readme)
        self.assertIn(f"**{goal - total} to go**", self.readme)
        self.assertIn(self.data["checked_on"], self.readme)
        self.assertIn(f"{100 * total / goal:.1f}%", self.readme)
        external_total = self.data["external_merged_total"]
        self.assertGreaterEqual(external_total, total)
        self.assertIn(f"**{external_total} merged public PRs outside `mangeshraut712` and `dayx61` repositories**", self.readme)
        self.assertIn(f"[All {total} merged PRs and merge dates]", self.readme)

    def test_five_cases_are_backed_by_merged_prs_and_tests(self):
        section = self.readme.split("#### Selected Engineering Impact", 1)[1].split("### More projects", 1)[0]
        cases = self.data["selected_case_studies"]
        records = {record["url"]: record for record in self.data["merge_evidence"]}
        self.assertEqual(len(cases), 5)
        self.assertIn(f'Five case studies selected from those {self.data["total"]} merges', section)
        self.assertEqual(len({case["url"] for case in cases}), 5)
        self.assertEqual(section.count("<summary>"), 5)
        self.assertEqual(section.count("</details>"), 5)
        for case in cases:
            self.assertIn(case["url"], records)
            self.assertIn(case["url"], section)
            self.assertRegex(case["merge_commit"], r"^[0-9a-f]{40}$")
            self.assertTrue(case["test_paths"])
            repo = records[case["url"]]["repo"]
            for path in case["test_paths"]:
                self.assertIn(f'https://github.com/{repo}/blob/{case["merge_commit"]}/{path}', section)


if __name__ == "__main__":
    unittest.main()
