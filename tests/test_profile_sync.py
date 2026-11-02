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


if __name__ == '__main__':
    unittest.main()
