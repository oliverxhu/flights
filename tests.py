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

driver = webdriver.PhantomJS(r"C:\Users\HF_BI\node_modules\phantomjs\lib\phantom\bin\phantomjs.exe")
driver.set_window_size(1024, 768)
driver.get("https://duckduckgo.com/")
pagesource = driver.page_source
with open('testest.txt', 'w+') as file:
    file.write(str(pagesource.encode('utf8')))