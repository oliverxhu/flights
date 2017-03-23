""" Unlimited number of processes multiprocessing example """
# if __name__ == '111__main__':
#     jobs = []
#     for i in itertools.islice(dateRange, 10):
#         p = multiprocessing.Process(target=getDataWorker.workerFromSydney, args=(i, toAirport))
#         jobs.append(p)
#         p.start()
#     print(jobs)

""" Navigating Google Flights Example """

import functions as fn
from selenium import webdriver
import time
from datetime import timedelta, date

template = 'https://www.google.com/flights/?curr=AUD#search;' + \
           'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s'

irl = 'https://www.google.com/flights/?curr=AUD#search;f=SYD;t=TYO;d=2017-07-25;r=2017-07-26;tt=o;mp=1000;so=p'
url = template % {'fromAirport': 'SYD',
                  'toAirport': 'TYO',
                  'depDate': '2017-08-28',
                  'maxPrice': 1000,
                  'sortBy': 'p'}


currentYear = int(time.strftime('%Y'))
currentMonth = int(time.strftime('%m'))
currentDay = int(time.strftime('%d'))
startDate = date(currentYear, currentMonth+4, currentDay)  # first date to scrape
endDate = startDate + timedelta(days=10)  # last date to scrape

dateList = fn.dateGenerator(startDate, endDate)

driver = webdriver.Firefox()
driver.get(url)
time.sleep(7)
pagesource = driver.page_source
with open('pagesource1.txt', 'w+') as file:
    file.write(str(pagesource.encode('utf8')))
element = driver.find_element_by_class_name('OMOBOQD-G-b')
element.click()
time.sleep(7)
pagesource = driver.page_source
with open('pagesource2.txt', 'w+') as file:
    file.write(str(pagesource.encode('utf8')))
element.click()
time.sleep(7)
pagesource = driver.page_source
with open('pagesource3.txt', 'w+') as file:
    file.write(str(pagesource.encode('utf8')))
driver.quit()