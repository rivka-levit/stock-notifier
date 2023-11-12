"""
Clients to browse in Internet
"""

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


class ChromeClient(webdriver.Chrome):
    """Chrome driver with options that can be connected to a certain url."""

    def __init__(self, chrome_drv: str = 'D:\\DEV\\chromedriver.exe') -> None:

        options = webdriver.ChromeOptions()
        options.add_argument('disable-infobars')
        options.add_argument('start-maximized')
        options.add_argument('disable-dev-shm-usage')
        options.add_argument('no-sandbox')
        options.add_argument('disable-gpu')
        options.add_argument('headless')  # Without open browser window
        options.add_argument('disable-blink-features=AutomationControlled')
        options.add_experimental_option('excludeSwitches',
                                        ['enable-automation'])

        service = Service(chrome_drv)

        super().__init__(service=service, options=options)
