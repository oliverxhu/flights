import multiprocessing as mp
import os
from selenium import webdriver
import time

os.chdir(r'C:\Users\HF_BI\Dropbox (Personal)\Flights\Flight Scraping\Output')

# multiprocessing

def worker(i):
    template = 'https://www.google.com/flights/?curr=AUD#search;' + \
               'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s'
    fromAirport = 'SYD'
    toAirport = 'TYO,OSA,FUK'
    depDate = '2017-08-26'
    maxPrice = 1000
    sortBy = 'p'
    sleepTime = 10

    url = template % {'fromAirport': fromAirport, 'toAirport': toAirport, 'depDate': depDate, 'maxPrice': maxPrice,
                      'sortBy': sortBy}

    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(sleepTime)
    pageSource = driver.page_source
    driver.quit()
    with open('pageSource%s.txt'%i, 'w+') as file:
        file.write(str(pageSource.encode('utf8')))

if __name__ == '__main__':
    jobs = []
    for i in range(3):
        p = mp.Process(target=worker, args=(i,))
        jobs.append(p)
        p.start()
    print(jobs)

