# IRCTC Tatkal Booking Automation

Selenium-based automation tool that books IRCTC train tickets —
handles login, train search, seat selection, and passenger details
automatically, stopping at the payment page for manual completion.

## Why I built this
Tatkal booking opens at a specific time and if you're in a meeting
or commuting you'll miss it. This lets you schedule the script the
night before. It handles everything automatically and stops at the
payment page so you can complete it from your phone wherever you are.

## Tech stack
- Python
- Selenium WebDriver
- WebDriverWait / Expected Conditions
- webdriver-manager

## How to run
1. Clone the repo
2. Create a config.py file using config.example.py as reference
3. pip install selenium webdriver-manager
4. Schedule script using Task Scheduler (Windows) or cron (Linux) to run at:
   - 10:00am for AC classes (1A, 2A, 3A, CC)
   - 11:00am for non-AC classes (SL, 2S)
   one day before departure
5. python main.py

## How it works
- Logs into IRCTC automatically
- Searches for your configured train and date
- Selects seat class and checks availability
- Fills in passenger details
- Stops at payment page for manual completion

## Notes
- Script stops at the payment page with a 5 minute window for manual completion
- This is a demo project — payment step is intentionally left for manual action
- config.py must be created locally and is intentionally excluded from this repo
