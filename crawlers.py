"""
Crawlers to scrape data from sites.
"""

from selenium.webdriver.common.by import By
from clients import ChromeDriver
import time


class CbxCrawler:
    """Receive data from Zagreb Stock Exchange."""

    def __init__(self):
        self.driver = ChromeDriver()
        self.url = 'https://zse.hr/en/indeks-366/365?isin=HRZB00ICBEX6'

    def get_trend(self):
        """Scrape trend percentage."""

        self.driver.get(self.url)
        time.sleep(2)
        trend = self.driver.find_element(
            By.XPATH,
            '//span[contains(@class, "stock-trend")]'
        ).text

        return self.clean_trend(trend)

    @staticmethod
    def clean_trend(text_value):
        """Returns only float number of the string."""

        return float(text_value[:-2])
