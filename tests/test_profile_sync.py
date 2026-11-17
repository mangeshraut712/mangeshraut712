"""Accuracy regressions for public inventory and cached usage display."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
from xml.etree import ElementTree as ET

SPEC = importlib.util.spec_from_file_location('sync', Path(__file__).resolve().parents[1] / 'scripts/update_neofetch.py')
sync = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(sync)


class ProfileSyncTests(unittest.TestCase):
    def test_cached_periods_keep_original_dates(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'snapshot.json'
            path.write_text(json.dumps({'as_of': '2026-10-01', 'week_start': '2026-09-28',
                'synced_at': '2026-10-01T12:00:00Z', 'today_tokens': 1200, 'week_tokens': 2000}))
            with patch.object(sync, 'WBM_SNAPSHOT_PATH', path):
                burn = sync.burn_from_snapshot()
        self.assertTrue(burn['cached'])
        self.assertEqual(burn['synced_at'], '2026-10-01T12:00:00Z')
        self.assertIn('cached day 2026-10-01', burn['burn_today_data'])
        self.assertIn('cached week 2026-09-28', burn['burn_week_data'])
        self.assertIn('est.', burn['burn_lifetime_data'])

    def test_private_repositories_excluded_across_pages(self):
        pages = [{'user': {'repositories': {'nodes': [{'name': 'public', 'isPrivate': False},
            {'name': 'secret', 'isPrivate': True}], 'pageInfo': {'hasNextPage': True, 'endCursor': 'cursor'}}}},
            {'user': {'repositories': {'nodes': [{'name': 'public-fork', 'isPrivate': False}],
                'pageInfo': {'hasNextPage': False, 'endCursor': None}}}}]
        with patch.object(sync, 'gql', side_effect=pages) as gql:
            repos = sync.fetch_owned_repos()
        self.assertEqual([repo['name'] for repo in repos], ['public', 'public-fork'])
        self.assertEqual(gql.call_args_list[1].args[1]['after'], 'cursor')

    def test_refresh_preserves_authored_benchmark_card(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            readme = root / 'README.md'
            readme.write_text('### Engineering metrics\n\n### Open-source contributions\n')
            card = root / 'metrics-dark.svg'
            card.write_text('<svg><text id="vad_latency_gate">≤100ms</text></svg>')
            original = card.read_text()
            with patch.object(sync, 'ROOT', root), patch.object(sync, 'README_PATH', readme):
                sync.update_readme({'stack_icons': 'py', 'lifetime_raw': 9999,
                                    'synced_at': '2026-11-02T00:00:00Z'})
            self.assertEqual(card.read_text(), original)
            self.assertNotIn('9,999', readme.read_text())
            self.assertNotIn('contribution-calendar totals', readme.read_text())
            self.assertNotIn('personal 50-PR goal', readme.read_text())

    def test_cached_banner_preserves_source_time(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / 'banner.svg'
            path.write_text('<svg xmlns="http://www.w3.org/2000/svg"><text id="wbm_as_of"/><text id="burn_today_data"/></svg>')
            burn = {'cached': True, 'synced_at': '2026-10-01T12:00:00Z',
                'burn_rank_data': '#1', 'burn_lifetime_data': '1K',
                'burn_today_data': 'cached day 2026-10-01 · 1K tokens', 'burn_week_data': 'cached week'}
            with patch.object(sync, 'SVG_PATHS', [path]):
                sync.update_svgs(burn=burn)
            text = path.read_text()
        self.assertIn('WBM cached · 2026-10-01 12:00:00Z', text)
        self.assertIn('cached day 2026-10-01', text)

    def test_update_readme_refreshes_trajectory_table_and_cache_busters(self):
        with tempfile.TemporaryDirectory() as directory:
            readme = Path(directory) / 'README.md'
            readme.write_text(
                '<img src="banner-dark.svg?v=old" />\n'
                '<img src="trajectory-dark.svg?v=old" />\n'
                "Figures from the [repository's GitHub snapshot](data/github-snapshot.json), collected **2026-11-17 16:30 IST**:\n\n"
                '| 2026 activity | Count |\n'
                '| --- | ---: |\n'
                '| Contribution-calendar total (YTD) | 6,524 |\n'
                '| Rolling 1-year calendar contributions | 7,056 |\n'
                '| Commits | 4,077 |\n'
                '| Pull requests | 1,731 |\n'
                '| Reviews | 349 |\n'
                '| Issues | 265 |\n'
                '| All-time contributions | 8,171 |\n'
            )
            stats = {
                'stack_icons': 'py',
                'ytd_raw': 6554,
                'rolling_1yr_raw': 7087,
                'commits_raw': 4094,
                'prs_raw': 1744,
                'reviews_raw': 351,
                'issues_raw': 265,
                'lifetime_raw': 8201,
                'synced_at': '2026-11-17T19:00:00Z',
            }
            with patch.object(sync, 'README_PATH', readme):
                sync.update_readme(stats)
                sync.bump_banner_cache_buster('2026111719')
            updated = readme.read_text()
        self.assertIn('banner-dark.svg?v=2026111719', updated)
        self.assertIn('trajectory-dark.svg?v=2026111719', updated)
        self.assertIn('collected **2026-11-17 19:00 UTC**', updated)
        self.assertIn('| Contribution-calendar total (YTD) | 6,554 |', updated)
        self.assertIn('| Rolling 1-year calendar contributions | 7,087 |', updated)
        self.assertIn('| Commits | 4,094 |', updated)
        self.assertIn('| Pull requests | 1,744 |', updated)
        self.assertIn('| Reviews | 351 |', updated)
        self.assertIn('| All-time contributions | 8,201 |', updated)


if __name__ == '__main__':
    unittest.main()
