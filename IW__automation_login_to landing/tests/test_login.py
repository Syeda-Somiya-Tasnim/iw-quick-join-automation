import time
from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage

def test_login_success(driver, config):
    driver.get(config["base_url"])

    login = LoginPage(driver)
    login.assert_on_login_page()
    login.login(config["username"], config["password"])

    # Force reload app after OAuth redirect (stabilizes SPA)
    driver.get(config["base_url"])

    dashboard = DashboardPage(driver)
    dashboard.wait_until_app_loaded()

    print("LOGIN SUCCESS")
    print("FINAL_URL =", driver.current_url)

    driver.save_screenshot("after_login_success.png")

    if config.get("pause_seconds", 0) > 0:
        time.sleep(config["pause_seconds"])
