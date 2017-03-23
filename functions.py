""" 1) Scraping Functions """


def dateGenerator(startDate, endDate):
    """ Create a generator function for the dates to loop through """
    from datetime import timedelta
    dateList = []
    for ndays in range((endDate - startDate).days):
        dateList.append(str(startDate + timedelta(days=ndays)))
    return dateList


def combinationGenerator(airportList, dateList):
    return [[airport, date] for airport in airportList for date in dateList]


def getAirports():
    """Reads the list of airports from the CSV airports.csv"""
    import pandas as pd
    df = pd.read_csv('Airports.csv')
    return list(df['iata_code'])


""" 2) Parsing Functions """

from bs4 import BeautifulSoup


def appendList(ls, bsFindObj):
    if bsFindObj is None:
        ls.append(None)
    else:
        ls.append(bsFindObj.text)
    return ls


def getAllInfo(flightSoup):
    hrefs = []
    prices = []
    durations = []
    stops = []
    stopDetails = []
    airports = []
    services = []
    for flight in flightSoup.findAll('a'):  # get hrefs
        hrefs.append(flight.get('href'))
        for price in flight.findChildren()[2]:  # get prices
            prices.append(price)
        duration = flight.find('div', class_='OMOBOQD-d-E')  # get durations
        durations.append(duration.text)
        stop = flight.find('div', class_='OMOBOQD-d-Qb')  # get stops
        stops.append(stop.text)
        stopDetail = flight.find('div', class_='OMOBOQD-d-Z')  # get stop details
        appendList(stopDetails, stopDetail)
        airport = flight.find('div', class_='OMOBOQD-d-Ib')  # get airports
        airports.append(airport.text)
        for company in flight.findAll('div', class_='OMOBOQD-d-j'):  # get airline
            if len(company.findAll('div')) > 0:
                for subcompany in company.findAll('div', class_='OMOBOQD-d-k'):
                    content = ""
                    for contents in subcompany.contents:
                        if str(contents) != '<br/>':
                            content += str(contents) + ", "
                    services.append(content.rstrip()[:-1])

            else:
                services.append(company.text)
    return hrefs, prices, durations, stops, stopDetails, airports, services


def getTimeInfo(flightSoup):
    data = []
    times = []
    for flight in flightSoup.findAll('a'):
        for timeData in flight.findChildren()[4]:
            data.append(str(timeData))
    for element in data:
        elements = BeautifulSoup(element, 'lxml')
        for spans in elements.findAll('div', class_='OMOBOQD-d-Zb'):
            times.append(spans.text)
    return times
