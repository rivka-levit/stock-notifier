"""
Watch for the signal from stock exchange.
"""

import time
from utils.crawlers import CbxCrawler


class CbxWatcher:
    """Watch for Cbx trend."""

    def __init__(self):
        self.crawler = CbxCrawler()

    def match(self, condition: str, target_value):
        """Return True if the trend match the conditions."""

        self._valid_inputs(condition, target_value)
        num = trend = float(target_value)

        if condition == 'gt':
            return self._wait_greater_value(trend, num)
        if condition == 'lt':
            return self._wait_less_value(trend, num)

    def _wait_greater_value(self, trend, target):
        """Scrape stock price until it is greater, then the number."""

        while trend <= target:
            trend = self.crawler.get_trend()
            time.sleep(10)

        return trend

    def _wait_less_value(self, trend, target):
        """Scrape stock price until it is less, then the number."""

        while trend >= target:
            trend = self.crawler.get_trend()
            time.sleep(10)

        return trend

    @staticmethod
    def _valid_inputs(cond: str, value: str | int | float):
        """Check condition and price value passed with inputs."""

        # Check if the right condition has been passed
        if cond not in ('gt', 'lt'):
            raise ValueError('You must provide one of the conditions: '
                             '"gt" (greater then) or "lt" (less then)!')

        # Check if the target_price is in the right format
        try:
            float(value)
        except ValueError as e:
            raise ValueError('The target value must be a float number') from e
