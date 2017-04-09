import time
from selenium import webdriver
import functions as fn
import settings
import getDataMain1


def workerFromSydney(toAirport, fromAirport='SYD', sleepTimeInitial=settings.sleepTimeInitial,
                     sleepTime=settings.sleepTime, maxPrice=2000, sortBy='p'):
    """ 
    Worker that iterates through all the dates for each location and writes them to file 
    Parameters
    ----------
    toAirport: Google Flights formatted list of departure airports
    fromAirport: Google Flights formatted list of arrival airports
    sleepTimeInitial: Wait time after initially loading the website
    sleepTime: Wait time before extracting the page source
    maxPrice: maximum price of flights to scrape
    sortBy: Sort flights by. p = price
    """

    dateList = fn.dateGenerator(settings.startDate, settings.endDate)
    template = 'https://www.google.com/flights/?curr=AUD#search;' + \
               'f=%(fromAirport)s;t=%(toAirport)s;d=%(depDate)s;tt=o;mp=%(maxPrice)s;so=%(sortBy)s;eo=e'
    url = template % {'fromAirport': fromAirport,
                      'toAirport': toAirport,
                      'depDate': dateList[0],
                      'maxPrice': maxPrice,
                      'sortBy': sortBy}

    """ initial browser start """
    phantomJSpath=r"C:\Users\HF_BI\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe"
    driver = webdriver.PhantomJS()
    driver.get(url)
    time.sleep(sleepTimeInitial)
    try:
        # check if there are flights for that day, if there aren't, try the next airport
        driver.find_element_by_class_name('OMOBOQD-d-Ib')

    except Exception as e:
        # move on to the next airport
        if "Unable to find element with class name" not in e:
            print(e)
        print('%s has no flights' % toAirport)
        driver.quit()

    else:
        # write airport code to file
        pageSource = driver.page_source
        """ write initial date """
        with open(r'C:\Users\HF_BI\Documents\Oliver\Flight Output\%s\%s_%s_%s_pageSource.txt' % (
        settings.outPath, dateList[0], toAirport, fromAirport), 'w+') as file:
            file.write(str(pageSource.encode('utf8')))

        """ loop over the rest of the dates """
        for date in dateList[1:]:
            # go to the next date
            driver.find_element_by_class_name('OMOBOQD-G-b').click()  # go to the next date
            time.sleep(sleepTime)
            pageSource = driver.page_source

            # write file to computer only if you can expand it, ie. flights exist
            with open(r'C:\Users\HF_BI\Documents\Oliver\Flight Output\%s\%s_%s_%s_pageSource.txt' % (
            settings.outPath, date, toAirport, fromAirport), 'w+') as file:
                file.write(str(pageSource.encode('utf8')))





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
