import glob
import pandas as pd
from bs4 import BeautifulSoup
import functions as fn
import settings
import itertools as it
import os
# import pdb; pdb.set_trace()



''' Get page data from Google Flights'''

dfTotal = pd.DataFrame(columns=['fromAirport', 'toAirport', 'price', 'departureDates', 'time', 'duration',
                                'airport', 'href', 'stops', 'stopDetails', 'airline'])

fileList = glob.glob(r'C:\Users\HF_BI\Documents\Oliver\Flight Output\Output\*pageSource*')

for file in fileList:
    with open(file, 'r+') as readfile:
        pageSource = readfile.read()

    ''' Parse page data'''

    soup = BeautifulSoup(pageSource, 'lxml')

    # Best flights
    flights = []
    strFlight = ""
    for link in soup.findAll('a'):
        if 'google.com/flights/?curr=AUD#search' in str(link):
            flights.append(link)
            strFlight += str(link)

    flightSoup = BeautifulSoup(strFlight, 'lxml')

    '''Parsing rules for Google Flights'''

    hrefs, prices, durations, stops, stopDetails, airports, services = fn.getAllInfo(flightSoup)
    times = fn.getTimeInfo(flightSoup)

    filename = os.path.split(file)[1]
    depDate = filename.split('_')[0]
    fromAirport = filename.split('_')[2]
    toAirport = filename.split('_')[1]
    depDates = [depDate for i in range(len(hrefs))]
    print('depdates: ', depDates)
    print('fromAirport: ', fromAirport)
    print('toAirport: ', toAirport)
    print('hrefs: ', hrefs)
    print('prices: ', prices)
    print('durations: ', durations)
    print('stops: ', stops)
    print('stopDetails: ', stopDetails)
    print('airports: ', airports)
    print('services: ', services)

    ''' Returning data in a pandas dataframe '''
    df = pd.DataFrame({
                       'fromAirport': [fromAirport] * len(prices),
                       'toAirport':[toAirport] * len(prices),
                       'price': [int(x[2:].replace(',', '')) for x in prices],
                       'departureDates': depDates,
                       'time': times,
                       'duration': durations,
                       'airport': airports,
                       'href': hrefs,
                       'stops': stops,
                       'stopDetails': stopDetails,
                       'airline': services})

    dfTotal = pd.concat([dfTotal, df])

dfTotal.to_csv(r'C:\Users\HF_BI\Documents\Oliver\Flight Output\Output\Parsed\Details.csv', index=None)

