import time
from datetime import date, timedelta

currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth, currentDay)
endDate = startDate + timedelta(days=240)