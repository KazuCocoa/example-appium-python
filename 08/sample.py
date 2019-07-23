import unittest

from appium import webdriver
from selenium.common.exceptions import WebDriverException

# Run standard unittest base.
class TestIOSCreateSession(unittest.TestCase):
    IOS_BASE_CAPS = {
        'browserName': 'safari',
        'automationName': 'xcuitest',
        'platformName': 'iOS',
        'platformVersion': '12.2',
        'deviceName':'iPhone 8',
    }

    def test_simple_launch(self):
        self.driver = webdriver.Remote(
            command_executor='http://localhost:4723/wd/hub',
            desired_capabilities=self.IOS_BASE_CAPS
        )

        assert self.driver.title == 'Appium/welcome'

if __name__ == '__main__':
    unittest.main()
