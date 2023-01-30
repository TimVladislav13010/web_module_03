from time import time
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
    return tuple(result)


time_start = time()
a, b, c, d = factorize(128, 255, 99999, 10651060)
time_finish = time()

logger.debug(f"time funktion work - {time_finish - time_start}")
logger.debug(f"{a}\n{b}\n{c}\n{d}\n")

assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]


# time funktion work - 1.3906910419464111
# [1, 2, 4, 8, 16, 32, 64, 128]
# [1, 3, 5, 15, 17, 51, 85, 255]
# [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
# [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
