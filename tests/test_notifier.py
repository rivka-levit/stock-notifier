"""
Tests for notifiers.
"""
from unittest import TestCase
from unittest.mock import patch

from notifiers import CbxNotifier
from emails import EmailTrendNotification


class NotificationTests(TestCase):
    """Tests for notification of trend level match."""

    def setUp(self):
        self.ntf = CbxNotifier()
        self.mail = EmailTrendNotification()

    @patch('watchers.CbxWatcher.match')
    def test_notify_when_trend_match(self, patched_trend):
        """Test sending notification when the trend matches the value."""

        patched_trend.return_value = 0.17

        self.ntf.notify('gt', 0.15)
