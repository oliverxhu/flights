import time
from datetime import date, timedelta

# General settings

outDir = r'C:\Users\HF_BI\Dropbox (Personal)\Flight Scraping\Output'

# Scraping settings

iterationLimit = None  # limit number of jobs running. This should always be "None" except debugging
processNumber = 10  # number of concurrent browser instances to run on the computer

currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth, currentDay)  # first date to scrape
endDate = startDate + timedelta(days=240)  # last date to scrape
