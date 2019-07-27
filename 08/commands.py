self.driver = webdriver.Remote(
    command_executor='http://localhost:4723/wd/hub',
    desired_capabilities=self.IOS_BASE_CAPS
)

# Get page source
self.driver.page_source
