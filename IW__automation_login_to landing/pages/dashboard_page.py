import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class DashboardPage(BasePage):
    # Keycloak markers (must NOT exist after login)
    KEYCLOAK_FORM = (By.CSS_SELECTOR, "form#kc-form-login")
    KEYCLOAK_TITLE = (By.CSS_SELECTOR, "#kc-page-title")

    # CI app markers (from homepage HTML)
    APP_MANIFEST = (By.CSS_SELECTOR, "link[rel='manifest'][href*='manifest.json']")
    APP_HTML_THEME = (By.CSS_SELECTOR, "html[data-theme]")
    HELPSCOUT_BEACON = (By.CSS_SELECTOR, "script[src*='beacon-v2.helpscout.net'], script#beacon-1")

    def wait_until_app_loaded(self):
        end = time.time() + 90
        while time.time() < end:
            url = self.driver.current_url

            if "kcv24.innovationwithin.services" in url:
                time.sleep(0.5)
                continue

            if self.driver.find_elements(*self.KEYCLOAK_FORM) or self.driver.find_elements(*self.KEYCLOAK_TITLE):
                time.sleep(0.5)
                continue

            if (self.driver.find_elements(*self.APP_MANIFEST)
                or self.driver.find_elements(*self.APP_HTML_THEME)
                or self.driver.find_elements(*self.HELPSCOUT_BEACON)):
                return

            time.sleep(0.5)

        raise AssertionError(
            "Not on CI app after login within timeout.\n"
            f"Current URL: {self.driver.current_url}"
        )
