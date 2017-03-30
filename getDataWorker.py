import time
import getDataMain1
from selenium import webdriver
import functions as fn
import settings


def workerFromSydney(toAirport, fromAirport='SYD', sleepTimeInitial=settings.sleepTimeInitial,
                     sleepTime=settings.sleepTime, maxPrice=2000, sortBy='p'):
    """ Worker that iterates through all the dates for each location and writes them to file"""
    dateList = fn.dateGenerator(settings.startDate, settings.endDate)
    template = 'https://www.google.com/flights/?curr=AUD#search;' + \
               'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s'
    url = template % {'fromAirport': fromAirport,
                      'toAirport': toAirport,
                      'depDate': dateList[0],
                      'maxPrice': maxPrice,
                      'sortBy': sortBy}

    """ initial browser start """

    driver = webdriver.PhantomJS(r"C:\Users\HF_BI\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe")
    driver.get(url)
    time.sleep(sleepTimeInitial)
    pageSource = driver.page_source

    """ Create s3 folder """
    # to create folder (airport)

    """ write initial date """
    with open('%s/%s_%s_%s_pageSource.txt' % (settings.outPath, dateList[0], toAirport, fromAirport), 'w+') as file:
        file.write(str(pageSource.encode('utf8')))

    # getDataMain1.s3Client.put_object(Body=pageSource,
    #                                  Bucket='flights',
    #                                  Key='scrape/%s/%s_%s_%s_pageSource.txt' % (toAirport, dateList[0], toAirport,
    #                                                                             fromAirport))

    """ loop over the rest of the dates """
    for date in dateList[1:]:
        element = driver.find_element_by_class_name('OMOBOQD-G-b')
        element.click()
        time.sleep(sleepTime)
        pageSource = driver.page_source

        # write file to computer
        with open('%s/%s_%s_%s_pageSource.txt' % (settings.outPath, date, toAirport, fromAirport), 'w+') as file:
            file.write(str(pageSource.encode('utf8')))

        # write file to s3
        # getDataMain1.s3Client.put_object(Body=pageSource,
        #                                  Bucket='flights',
        #                                  Key='scrape/%s/%s_%s_%s_pageSource.txt' % (date, toAirport, fromAirport))
    driver.quit()


def workerToSydney(fromAirport, toAirport='SYD', sleepTimeInitial=15, sleepTime=12, maxPrice=1000, sortBy='p'):
    """ Worker that iterates through all the dates for each location and writes them to file"""
    dateList = fn.dateGenerator(settings.startDate, settings.endDate)
    template = 'https://www.google.com/flights/?curr=AUD#search;' + \
               'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s'
    url = template % {'fromAirport': fromAirport,
                      'toAirport': toAirport,
                      'depDate': dateList[0],
                      'maxPrice': maxPrice,
                      'sortBy': sortBy}

    """ initial browser start """
    driver = webdriver.Firefox()
    driver.get(url)
    time.sleep(sleepTimeInitial)
    pageSource = driver.page_source

    """ write initial date """
    with open('Output/Test/%s_%s_%s_pageSource.txt' % (dateList[0], toAirport, fromAirport), 'w+') as file:
        file.write(str(pageSource.encode('utf8')))

    """ loop over the rest of the dates """
    for date in dateList[1:]:
        element = driver.find_element_by_class_name('OMOBOQD-G-b')
        element.click()
        time.sleep(sleepTime)
        pageSource = driver.page_source

        with open('Output/%s_%s_%s_pageSource.txt' % (date, toAirport, fromAirport), 'w+') as file:
            file.write(str(pageSource.encode('utf8')))

    driver.quit()
