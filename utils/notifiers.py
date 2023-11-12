"""
Notifiers to wait for watcher matches and send notification.
"""
from utils.watchers import CbxWatcher
from utils.emails import EmailTrendNotification


class CbxNotifier:
    """Cbx index trend notifier."""

    def __init__(self):
        self.watcher = CbxWatcher()
        self.mail = EmailTrendNotification()

    def notify(self, direction: str, value: int | float | str) -> None:
        """Notify the user when the trend matches the value."""

        trend = self.watcher.match(direction, value)
        self.mail.send(trend)
