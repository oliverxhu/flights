import time
from datetime import date, timedelta

outDir = r'C:\Users\HF_BI\Dropbox (Personal)\Flight Scraping\Output'

currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth, currentDay)
endDate = startDate + timedelta(days=240)

def getAirports():
    import pandas as pd
    df = pd.read_csv('Airports.csv')
    return list(df['iata_code'])