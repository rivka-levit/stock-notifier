"""
Crawlers to scrape data from sites.
"""

from selenium.webdriver.common.by import By
from utils.clients import ChromeClient
import time


class CbxCrawler:
    """Receive data from Zagreb Stock Exchange."""

    def __init__(self):
        self.client = ChromeClient()
        self.url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'

    def get_trend(self):
        """Scrape trend percentage."""

        self.client.get(self.url)
        time.sleep(2)
        trend = self.client.find_element(
            By.XPATH,
            '//span[contains(@class, "stock-trend")]'
        ).text

        return self.clean_trend(trend)

    @staticmethod
    def clean_trend(text_value):
        """Returns only float number of the string."""

        return float(text_value[:-2])
