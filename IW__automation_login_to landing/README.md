# InnovationWithin CI - Selenium Automation (Pytest + POM)

This project automates login for InnovationWithin CI using **Selenium + Pytest + Page Object Model**.
It is built to handle **Keycloak (kcv24...) OAuth redirects** and **SPA behavior** reliably.

## Setup (Windows PowerShell)
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
