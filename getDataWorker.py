from selenium import webdriver
import time

def workerFromSydney(depDate, toAirport, fromAirport='SYD', sleepTime=15, maxPrice=1000, sortBy='p'):
    """Worker function to open pages and write to file"""
    temp = r'https://www.google.com/flights/?' + \
           'curr=AUD#search;f=SYD;t=HND,NRT,23K,KIX,ITM;d=2017-08-24;r=2017-08-26;tt=o;mp=1000;so=p'

    template = 'https://www.google.com/flights/?curr=AUD#search;' + \
        'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s'

    url = template % {'fromAirport': fromAirport,
                      'toAirport': toAirport,
                      'depDate': depDate,
                      'maxPrice': maxPrice,
                      'sortBy': sortBy}

    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(sleepTime)
    pageSource = driver.page_source
    driver.quit()

    with open('%s_%s_%s_pageSource.txt' % (depDate, fromAirport, toAirport), 'w+') as file:
        file.write(str(pageSource.encode('utf8')))

def workerToSydney(depDate, fromAirport, toAirport='SYD', sleepTime=15, maxPrice=1000, sortBy='p'):
    pass