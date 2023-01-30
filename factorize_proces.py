from time import time
from multiprocessing import Process, cpu_count
import logging


logger = logging.getLogger()
stream_handler = logging.StreamHandler()
logger.addHandler(stream_handler)
logger.setLevel(logging.DEBUG)


def factorize(number):
    result = list()

    result_list = list()
    result_list.append(number)
    result_number = number
    while True:
        result_number = result_number - 1

        if (number % result_number) == 0:
            result_list.insert(0, result_number)

        if result_number == 1:
            result.append(result_list)
            break
    logger.debug(f"{result}")
    return result


if __name__ == "__main__":
    logger.debug(f"Number cpu cores - {cpu_count()}")

    numbers = [128, 255, 99999, 10651060]

    processes = []

    time_start = time()
    for i in numbers:
        pr = Process(target=factorize, args=(i,))
        pr.start()
        processes.append(pr)
        logger.debug(f"{pr}")

    [el.join() for el in processes]
    time_finish = time()

    [print(el.exitcode, end=" ") for el in processes]
    logger.debug(f"Time funktion work - {time_finish - time_start}")
    logger.debug("End program")


# Number cpu cores - 4
# <Process name='Process-1' pid=6926 parent=6925 started>
# [[1, 2, 4, 8, 16, 32, 64, 128]]
# <Process name='Process-2' pid=6927 parent=6925 started>
# [[1, 3, 5, 15, 17, 51, 85, 255]]
# <Process name='Process-3' pid=6928 parent=6925 started>
# <Process name='Process-4' pid=6929 parent=6925 started>
# [[1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]]
# [[1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]]
# Time funktion work - 1.4098374843597412
# End program
# 0 0 0 0
# Process finished with exit code 0
