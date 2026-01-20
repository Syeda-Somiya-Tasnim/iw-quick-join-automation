import os
import time
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()

BASE_URL = os.getenv("IW_BASE_URL", "https://ci.innovationwithin.services/")
USERNAME = os.getenv("IW_USERNAME", "tasnim")
PASSWORD = os.getenv("IW_PASSWORD", "tasnim123@IW")


def force_set(driver, css, value):
    el = driver.find_element("css selector", css)
    driver.execute_script(
        """arguments[0].focus();
           arguments[0].value='';
           arguments[0].dispatchEvent(new Event('input',{bubbles:true}));
           arguments[0].value=arguments[1];
           arguments[0].dispatchEvent(new Event('input',{bubbles:true}));
           arguments[0].dispatchEvent(new Event('change',{bubbles:true}));""",
        el, value
    )


def main():
    options = Options()
    options.page_load_strategy = "eager"
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    driver.set_window_size(1280, 720)

    try:
        print("Going to:", BASE_URL)
        driver.get(BASE_URL)

        time.sleep(2)

        force_set(driver, "#username", USERNAME)
        force_set(driver, "#password", PASSWORD)

        u = driver.execute_script("return document.querySelector('#username')?.value")
        print("USERNAME_IN_FIELD =", u)
        print("URL(before submit) =", driver.current_url)

        driver.find_element("css selector", "#kc-login").click()

        last = ""
        end = time.time() + 90
        while time.time() < end:
            cur = driver.current_url
            if cur != last:
                print("URL changed ->", cur)
                last = cur
            time.sleep(0.2)

        print("\nFINAL URL =", driver.current_url)
        driver.save_screenshot("landing_url_debug.png")
        print("Saved screenshot: landing_url_debug.png")

        input("Press Enter to close browser...")
    finally:
        driver.quit()


if __name__ == "__main__":
    main()
