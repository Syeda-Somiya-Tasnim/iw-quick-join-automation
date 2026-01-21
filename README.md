# InnovationWithin CI - Selenium Automation (Pytest + POM)

This project automates login for InnovationWithin CI using **Selenium + Pytest + Page Object Model**.
It is built to handle **Keycloak (kcv24...) OAuth redirects** and **SPA behavior** reliably.
# IW Quick Join Bot Automation

## Overview

This project automates the **Quick Join Bot workflow** for customer discovery interviews at **Innovation Within**.

The automation ensures that scheduled customer discovery meetings are:
- Detected automatically from the dashboard
- Joined using a platform-managed automated participant (Quick Join Bot)
- Triggered without manual intervention after login

This project focuses on **end-to-end automation from login → dashboard → meeting detection → quick join initiation**, using **Python + Selenium** and **Page Object Model (POM)** architecture.

---

## Problem Statement

Customer discovery interviews are often missed due to:
- Manual calendar monitoring
- Manual meeting joining
- Missed recordings

The goal is to **eliminate manual effort** by automatically:
- Detecting upcoming meetings
- Joining meetings at the scheduled time using a bot

---

## Scope of Automation

### Implemented

✅ Login via Keycloak  
✅ Redirect to application landing page  
✅ Dashboard load verification  
✅ Calendar & Meeting Assistant page handling  
✅ Detection of most recent / upcoming meeting  
✅ Quick Join Bot toggle & join logic  
✅ Default Chrome automation (no custom driver paths or profiles)

### Out of Scope

❌ Actual Zoom audio/video recording  
❌ Transcript generation  
❌ Backend interview storage  
❌ OAuth token manipulation  

---

## Architecture

### Tech Stack
- **Language:** Python 3.10+
- **Automation Tool:** Selenium WebDriver
- **Test Framework:** Pytest
- **Design Pattern:** Page Object Model (POM)
- **Browser:** Google Chrome (default)

---

## Project Structure

iw-quick-join-automation/
│
├── pages/
│ ├── base_page.py # Common Selenium helpers
│ ├── login_page.py # Login actions
│ ├── dashboard_page.py # Dashboard & calendar logic
│
├── tests/
│ ├── test_login.py # Login validation test
│ ├── test_quick_join.py # Quick Join Bot automation test
│
├── config/
│ └── settings.py # Base URL & timeouts
│
├── tools/
│ └── find_landing_url.py # Debug helper for redirect tracking
│
├── .env.example # Environment variable template
├── requirements.txt
├── pytest.ini
└── README.md

---

## Setup Instructions

###  Clone Repository
```bash
git clone https://github.com/<your-username>/iw-quick-join-automation.git
cd iw-quick-join-automation
```

### Setup (Windows PowerShell)
```powershell
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
copy .env.example .env
```

## Run
```powershell
pytest -s
```

## Debug (if you want to SEE the page)
Edit `.env`:
- `HEADLESS=false`
- `PAUSE_SECONDS=10` (or any seconds)
- optional: `DETACH=true` (keeps Chrome open after pytest)

Then run:
```powershell
pytest -s
```

## Notes
- Uses webdriver-manager to always download a matching ChromeDriver.
- Uses IW_USERNAME/IW_PASSWORD env vars to avoid Windows USERNAME env var override.


## Key Automation Logic

### Login Handling
- Uses **JavaScript injection** to ensure credentials are properly set
- Handles **Keycloak redirect instability**
- Waits for **application-level markers** instead of fixed delays

---

### Dashboard Detection
- Confirms successful exit from **Keycloak**
- Validates landing on the **Innovation Within application**
- Detects **calendar entries dynamically** from the dashboard

---

### Quick Join Bot
- Identifies the **most recent or upcoming meeting**
- Automatically **scrolls to the meeting element**
- Toggles **“Automatically join meeting”** switch
- Initiates **join action** when applicable

---

## Reliability Measures
- Uses **explicit waits** instead of `sleep()`
- Monitors **URL transitions** to ensure correct navigation
- Performs **UI state verification** before actions
- Implements **graceful timeout handling**
- Captures **screenshots on failure** for debugging

---

## Why Selenium (Not API / Playwright)
- Google OAuth & Keycloak involve **complex UI flows**
- Bot join behavior is **entirely UI-driven**
- Platform-managed participant requires **browser context**
- Selenium offers **maximum browser compatibility** and stability

---

## Known Limitations
- Manual approval may be required if **Google OAuth prompts appear**
- Meeting join depends on **meeting availability timing**
- UI changes may require **selector updates**

---

## Future Improvements
- Headless bot with **persistent session**
- **Parallel test execution**
- **Zoom SDK integration**
- Meeting **recording verification**
- **CI pipeline integration** (GitHub Actions)
