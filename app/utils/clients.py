"""
Clients to browse in Internet
"""

from selenium import webdriver


class RemoteChromeDriver:

    def __init__(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('disable-infobars')
        self.options.add_argument('start-maximized')
        self.options.add_argument('disable-dev-shm-usage')
        self.options.add_argument('no-sandbox')
        self.options.add_argument('disable-gpu')
        self.options.add_argument('headless')  # Without open browser window
        self.options.add_argument('disable-blink-features=AutomationControlled')
        self.options.add_experimental_option('excludeSwitches',
                                             ['enable-automation'])

    def get_driver(self):
        return webdriver.Remote(
            command_executor='http://chrome:4444',
            options=self.options
        )
