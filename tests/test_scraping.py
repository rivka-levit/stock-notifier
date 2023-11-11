"""
Tests for Chrome client.
"""

import unittest

from clients import ChromeDriver


class ChromeTests(unittest.TestCase):
    """Tests for Chrome driver."""

    def setUp(self):
        self.driver = ChromeDriver()

    def test_chrome_driver_works(self):
        self.driver.get("https://www.google.co.il/")
        self.assertIn("Google", self.driver.title)
