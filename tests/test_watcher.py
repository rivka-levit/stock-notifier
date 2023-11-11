"""
Tests for watchers.
"""
from unittest import TestCase
from unittest.mock import patch

from watchers import CbxWatcher


class CbxWatcherTests(TestCase):
    """Tests for CBX watcher."""

    def setUp(self):
        self.watcher = CbxWatcher()

    @patch('time.sleep')
    @patch('crawlers.CbxCrawler.get_trend')
    def test_watcher_check_trend(self, mock_trend, patched_sleep):
        """Test the watcher scrapes the trend and notify when it matches."""

        mock_trend.return_value = -0.28
        patched_sleep.return_value = 0

        self.assertTrue(self.watcher.match('lt', '-0.1'))

        mock_trend.return_value = 0.3

        self.assertTrue(self.watcher.match('gt', '0.1'))
