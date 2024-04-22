#!/usr/bin/env python3
''' Description: Import wait_random from the previous python file that
    you’ve written and write an async routine called wait_n that takes
    in 2 int arguments: max_delay and n. You will spawwn wait_random n
    times with the specified max_delay. wait_n should return the list
    of all the delays(float values). The list of the delays should be
    in ascending order without using sort() because of concurrency.
    Arguments: n: int, max_delay: int = 10
'''

import asyncio

from typing import List

import random

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int = 10) -> List[float]:
    """ Waiting up for ran delay until the max_delay, and to
    returns list of all the actual delays that occurred"""
    spawn_lss = []
    delays_ls = []
    for a in range(n):
        delayedd_taskk = asyncio.create_task(wait_random(max_delay))
        delayedd_taskk.add_done_callback(lambda x: delays_ls.append(x.result()))
        spawn_lss.append(delayedd_taskk)

    for spawwn in spawn_lss:
        await spawwn

    return delays_ls
