import functions as fn
import settings
import getDataWorker
import multiprocessing
import itertools
import os

os.chdir(r'C:\Users\HF_BI\Dropbox (Personal)\Flight Scraping\Output')

dateRange = fn.dateGenerator(settings.startDate, settings.endDate)

toAirport = 'TYO,OSA,FUK'

if __name__ == '__main__':
    jobs = []
    for i in itertools.islice(dateRange, 10):
        p = multiprocessing.Process(target=getDataWorker.workerFromSydney, args=(i, toAirport))
        jobs.append(p)
        p.start()
    print(jobs)