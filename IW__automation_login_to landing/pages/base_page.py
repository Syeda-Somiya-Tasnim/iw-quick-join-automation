from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self, driver, timeout=25):
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)

    def goto(self, url: str):
        self.driver.get(url)

    def wait_visible(self, by_locator):
        return self.wait.until(EC.visibility_of_element_located(by_locator))

    def wait_present(self, by_locator):
        return self.wait.until(EC.presence_of_element_located(by_locator))

    def wait_url_contains(self, text: str):
        return self.wait.until(EC.url_contains(text))
