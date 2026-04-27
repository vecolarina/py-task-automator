# Py Task Automator 🤖

A Python automation tool that monitors a folder for new CSV files,
automatically processes and cleans them, and sends an email summary
report — all without any manual intervention.

Built by a working Python Developer with real automation experience
in both healthcare and business systems.

---

## Features
- 👁️ Automatically watches a folder for new CSV files
- 🧹 Cleans data on detection (strips whitespace, drops empty rows)
- 📊 Generates a full summary report (row count, columns, null values, stats)
- 💾 Saves cleaned version of the file automatically
- 📧 Sends email notification with full summary report
- ⏳ Runs continuously in the background until stopped

---

## Requirements
- Python 3.8+
- Gmail account (for email notifications)
- Gmail App Password (not your real Gmail password)

---

## Installation

1. Clone the repository:
   git clone https://github.com/vecolarina/py-task-automator.git
   cd py-task-automator

2. Install dependencies:
   pip install -r requirements.txt

3. Configure your settings in config.py:
   WATCH_FOLDER = "./watch_folder"
   OUTPUT_FOLDER = "./sample"
   EMAIL_SENDER = "your@gmail.com"
   EMAIL_PASSWORD = "your_app_password"
   EMAIL_RECIPIENT = "recipient@gmail.com"

4. Run:
   python watcher.py

---

## How It Works
1. Script watches the watch_folder/ directory continuously
2. When a new CSV file is dropped into the folder:
   - File is read and cleaned automatically
   - Cleaned version is saved to sample/ folder
   - Email notification with full summary is sent
3. Process repeats for every new CSV file detected

---

## Setting Up Gmail App Password
1. Go to your Google Account settings
2. Search for "App Passwords"
3. Generate a new App Password for "Mail"
4. Copy and paste it into config.py as EMAIL_PASSWORD
   (Never use your real Gmail password)

---

## Sample Input
A sample CSV file is provided in sample/sample_input.csv
containing real-world data quality issues for testing:
- Valid and invalid email formats
- Valid and invalid PH phone numbers
- Duplicate records
- Null values

---

## Tech Stack
- Python 3
- watchdog
- pandas
- openpyxl
- smtplib (built-in)

---

## Use Cases
- Automated hospital data processing
- Business report automation
- ETL pipeline monitoring
- Any repetitive CSV handling task

---

Built by Von Adrian Colarina
Python Developer | Automation Specialist
github.com/vecolarina