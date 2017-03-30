import itertools
import multiprocessing
import functions as fn
import getDataWorker
import settings
import boto3

""" Connect to AWS s3 """
# try:
#     s3Client = boto3.client('s3',
#                             aws_access_key_id=settings.AWS_ACCESS_KEY_ID,
#                             aws_secret_access_key=settings.AWS_SECRET_ACCESS_KEY)
# except:
#     print("error s3 connection failed")


dateList = fn.dateGenerator(settings.startDate, settings.endDate)
airportList = fn.getAirports()

combinations = fn.combinationGenerator(airportList, dateList)


if __name__ == '__main__':
    # Start 1st one in firefox, start the rest in a new tab...
    pool = multiprocessing.Pool(processes=settings.processNumber)
    for airport in itertools.islice(airportList, 0, settings.iterationLimit):
        pool.apply_async(getDataWorker.workerFromSydney, args=(airport,))
        # pool.apply_async(getDataWorker.workerToSydney, args=(airport,))
    pool.close()
    pool.join()


# if __name__ == '__main__':
#     pool = multiprocessing.Pool(processes=settings.processNumber)
#     for comb in itertools.islice(combinations, 0, settings.iterationLimit):
#         pool.apply_async(getDataWorker.workerFromSydney, args=(comb[0], comb[1],))
#     pool.close()
#     pool.join()
