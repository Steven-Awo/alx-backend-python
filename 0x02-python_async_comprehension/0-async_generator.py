#!/usr/bin/env python3
''' Task: A coroutine called async_generator that takes no
    arguments. The coroutine will loop 10 times, each time
    asynchronously wait 1 second, then yield a random
    number between 0 and 10. Use the random module.
'''

from asyncio import sleep

from typing import Generator

from random import random

async def async_generator() -> Generator[float, None, None]:
    ''' A generator that does yields a random value thats
    between 0 and 10 for every second, occuring 10 times. '''
    for a in range(10):
        await sleep(1)
        yield 10 * random()
