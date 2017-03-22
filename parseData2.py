import functions as fn
from bs4 import BeautifulSoup
import os
import itertools as it
import pandas as pd
import glob
import sys

os.chdir(r'C:\Users\HF_BI\Dropbox (Personal)\Flight Scraping\Output')

''' Get page data from Google Flights'''

fileList = glob.glob('*pageSource.txt*')

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

    depDate = file[:10]
    depDates = [depDate for i in range(len(hrefs))]
    print(depDates)
    print(hrefs)
    ''' Returning data in a pandas dataframe'''
    # df = pd.DataFrame({
    #                    'price':[int(x[2:]) for x in prices],
    #                    'departureDates':depDates,
    #                    'time':times,
    #                    'duration':durations,
    #                    'airport':airports,
    #                    'href':hrefs,
    #                    'stops':stops,
    #                    'stopDetails':stopDetails,
    #                    'airline':services})
    #
    # print(df.head())
    # df.to_csv('Parse/data.csv', index=None)

