"""
Tests for Chrome client.
"""

import unittest

from utils.clients import RemoteChromeDriver
from utils.crawlers import CbxCrawler


class ScrapingTests(unittest.TestCase):
    """Tests for Chrome driver."""

    def setUp(self):
        self.client = RemoteChromeDriver()

    def test_chrome_driver_works(self):
        """Test chrome driver access the page and get the response."""

        driver = self.client.get_driver()
        driver.get('https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6')
        title = driver.title
        driver.quit()

        self.assertIn("CROBEX", title)

    def test_crawler_scrapes_trend(self):
        """Test the crawler returns float value of index change."""

        crawler = CbxCrawler()
        trend = crawler.get_trend()

        self.assertIsInstance(trend, float)
