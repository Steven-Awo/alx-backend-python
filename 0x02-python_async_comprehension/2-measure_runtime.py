#!/usr/bin/env python3
''' Desription: Import async_comprehension from the previous file and write a
    measure_runtime coroutine that will execute async_comprehension four
    times in parallel using asyncio.gather.measure_runtime should measure
    the total runtime and return it.Notice that the total runtime is
    roughly 10 seconds, explain it to yourself.
'''

from time import time

from asyncio import gather

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    ''' Measuring the runtime thats of async_comprehension
    that was executed 4 times in parallel. '''
    the_first_time = time()
    await gather(async_comprehension(), async_comprehension(),
                 async_comprehension(), async_comprehension())
    the_next_time = time()

    return the_next_time - the_first_time
