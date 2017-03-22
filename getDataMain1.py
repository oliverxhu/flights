import functions as fn
import parameters
import getDataWorker
import multiprocessing
import itertools

dateList = fn.dateGenerator(parameters.startDate, parameters.endDate)

airportList = parameters.getAirports()

combinations = fn.airportGenerator(airportList, dateList)

if __name__ == '__main__':
    pool = multiprocessing.Pool(processes=10)
    for comb in itertools.islice(combinations, 20):
        pool.apply_async(getDataWorker.workerFromSydney, args=(comb[0], comb[1], ))
    pool.close()
    pool.join()
