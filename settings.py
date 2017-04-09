import time
from datetime import date, timedelta

# Scraping settings

iterationLimit = 20  # limit number of airports to run. This should be "None" to run all airports
processNumber = 10  # number of concurrent browser instances to run on the computer
sleepTimeInitial = 15
sleepTime = 9
outPath = 'Output'

currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth, currentDay) + timedelta(days=1)  # first date to scrape = tomorrow
endDate = startDate + timedelta(days=240)  # last date to scrape)

AWS_ACCESS_KEY_ID = ''
AWS_SECRET_ACCESS_KEY = ''
