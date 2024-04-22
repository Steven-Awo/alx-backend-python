#!/usr/bin/env python3

''' Description: Take the code from wait_n and alter it into a new function
                 task_wait_n. The code is nearly identical to wait_n except
                 task_wait_random is being called.
    Arguments: n: int, max_delay: int = 10
'''

from typing import List

import random

import asyncio


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int = 10) -> List[float]:
    '''Executing the task_wait_random and then to return the
    sorted list of the delays'''
    spawning_list = []
    delaying_list = []
    for a in range(n):
        delayedd_task = task_wait_random(max_delay)
        delayedd_task.add_done_callback(lambda x: delaying_list.append(x.result()))
        spawning_list.append(delayedd_task)

    for spawner in spawning_list:
        await spawner

    return delaying_list
