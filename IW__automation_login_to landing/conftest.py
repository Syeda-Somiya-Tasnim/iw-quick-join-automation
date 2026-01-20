import os
import pytest
from dotenv import load_dotenv

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

load_dotenv()


@pytest.fixture(scope="session")
def config():
    return {
        "base_url": os.getenv("IW_BASE_URL", "https://ci.innovationwithin.services/").strip(),
        "username": os.getenv("IW_USERNAME", "tasnim").strip(),
        "password": os.getenv("IW_PASSWORD", "tasnim123@IW").strip(),
        "headless": os.getenv("HEADLESS", "false").lower() == "true",
        "detach": os.getenv("DETACH", "false").lower() == "true",
        "pause_seconds": int(os.getenv("PAUSE_SECONDS", "0") or "0"),
    }


@pytest.fixture()
def driver(config):
    options = Options()
    options.page_load_strategy = "eager"  # better for SPA apps

    # Reduce autofill / password manager prompts
    options.add_argument("--disable-features=AutofillServerCommunication")
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-notifications")

    if config["headless"]:
        options.add_argument("--headless=new")

    # Keep Chrome open after the test (handy for debugging)
    if config["detach"]:
        options.add_experimental_option("detach", True)

    service = Service(ChromeDriverManager().install())
    drv = webdriver.Chrome(service=service, options=options)
    drv.set_window_size(1280, 720)

    yield drv

    if not config["detach"]:
        drv.quit()
