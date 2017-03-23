import itertools
import multiprocessing

import functions as fn
import getDataWorker
import settings

dateList = fn.dateGenerator(settings.startDate, settings.endDate)
airportList = fn.getAirports()

combinations = fn.combinationGenerator(airportList, dateList)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=settings.processNumber)
    for airport in itertools.islice(airportList, 0, settings.iterationLimit):
        pool.apply_async(getDataWorker.workerFromSydney, args=(airport,))
        pool.apply_async(getDataWorker.workerToSydney, args=(airport,))
    pool.close()
    pool.join()


# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=settings.processNumber)
#     for comb in itertools.islice(combinations, 0, settings.iterationLimit):
#         pool.apply_async(getDataWorker.workerFromSydney, args=(comb[0], comb[1],))
#     pool.close()
#     pool.join()
