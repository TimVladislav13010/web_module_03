from time import time
from multiprocessing import Pool, cpu_count
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(*number):
    result = list()
    for num in number:
        result_list = list()
        result_list.append(num)
        result_number = num
        while True:
            result_number = result_number - 1

            if (num % result_number) == 0:
                result_list.insert(0, result_number)

            if result_number == 1:
                result.append(result_list)
                break
    return result


if __name__ == "__main__":
    logger.debug(f"Number cpu cores - {cpu_count()}")

    numbers = [128, 255, 99999, 10651060]

    time_start = time()

    with Pool(4) as p:
        print(p.map(factorize, numbers))

    time_finish = time()

    logger.debug(f"Time funktion work - {time_finish - time_start}")
    logger.debug("End program")


# Number cpu cores - 4
# Time funktion work - 1.6628994941711426
# End program
# [[[1, 2, 4, 8, 16, 32, 64, 128]], [[1, 3, 5, 15, 17, 51, 85, 255]], [[1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]], [[1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]]]
