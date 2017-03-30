import time
from datetime import date, timedelta

# Scraping settings

iterationLimit = 40  # limit number of airports to run. This should be "None" to run all airports
processNumber = 40  # number of concurrent browser instances to run on the computer
sleepTimeInitial = 30
sleepTime = 5
outPath = 'Output'

currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth, currentDay)  # first date to scrape
endDate = startDate + timedelta(days=240)  # last date to scrape

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
