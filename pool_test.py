import time
from multiprocessing import *


def sum_square(number):
    s = 0
    for i in range(number):
        s += i * i
    return s


if __name__ == '__main__':
    numbers = range(5)
    p = Pool()
    result = p.map(sum_square, numbers)
    p.close()
    p.join()
