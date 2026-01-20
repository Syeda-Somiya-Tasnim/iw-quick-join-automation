import time
from selenium.webdriver.common.by import By
from pages.base_page import BasePage

class LoginPage(BasePage):
    USERNAME = (By.CSS_SELECTOR, "#username")
    PASSWORD = (By.CSS_SELECTOR, "#password")
    SIGN_IN  = (By.CSS_SELECTOR, "#kc-login")
    TITLE    = (By.CSS_SELECTOR, "#kc-page-title")
    FORM     = (By.CSS_SELECTOR, "form#kc-form-login")

    ERROR_ALERTS = [
        (By.CSS_SELECTOR, ".alert-error"),
        (By.CSS_SELECTOR, ".pf-c-alert.pf-m-danger"),
        (By.CSS_SELECTOR, "#input-error"),
    ]

    def assert_on_login_page(self):
        self.wait_visible(self.TITLE)
        self.wait_present(self.FORM)
        assert "Sign in" in self.driver.find_element(*self.TITLE).text

    def _force_set_value_js(self, element, value: str):
        self.driver.execute_script(
            """arguments[0].focus();
               arguments[0].value = '';
               arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
               arguments[0].value = arguments[1];
               arguments[0].dispatchEvent(new Event('input', {bubbles:true}));
               arguments[0].dispatchEvent(new Event('change', {bubbles:true}));""",
            element, value
        )

    def login(self, username: str, password: str):
        user_el = self.wait_visible(self.USERNAME)
        pass_el = self.wait_visible(self.PASSWORD)

        self._force_set_value_js(user_el, username)
        self._force_set_value_js(pass_el, password)

        current = self.driver.execute_script("return arguments[0].value;", user_el)
        print("USERNAME_IN_FIELD =", current)
        print("URL(before submit) =", self.driver.current_url)

        self.driver.find_element(*self.SIGN_IN).click()

        self._wait_for_redirect_or_error()

    def _wait_for_redirect_or_error(self):
        end = time.time() + 60
        while time.time() < end:
            url = self.driver.current_url

            if "kcv24.innovationwithin.services" not in url:
                return

            for loc in self.ERROR_ALERTS:
                els = self.driver.find_elements(*loc)
                if els:
                    texts = [e.text.strip() for e in els if e.is_displayed() and e.text.strip()]
                    if texts:
                        raise AssertionError("Login failed. Keycloak error: " + " | ".join(texts))

            time.sleep(0.3)

        raise AssertionError(
            "Login submit happened but did not leave Keycloak within 60s. URL=" + self.driver.current_url
        )
