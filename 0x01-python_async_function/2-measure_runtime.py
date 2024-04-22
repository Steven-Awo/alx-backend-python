#!/usr/bin/env python3
''' Description: From the previous file, import wait_n into
    2-measure_runtime.py and create a measure_time function
    with integers n and max_delay as arguments that
    measures the total execution time for wait_n(n,
    max_delay), and returns total_time / n. Your function
    should return a float.
    Arguments: n: int, max_delay: int
'''

from time import time

from asyncio import run

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    ''' Returning the execution time that occured for wait_n
    given `n` and the `max_delay`. '''
    time_of_0 = time()
    run(wait_n(n, max_delay))
    time_of_1 = time()
    the_elapsedd_time = time_of_1 - time_of_0
    return the_elapsedd_time / n
