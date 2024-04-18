#!/usr/bin/env python3
''' Description: Accepts the float thats a multiplier as an argument
                 and returns a function that then multiplies a
                 float by the multiplier
    Parameters: multiplier: float
'''

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    ''' Outputing the function that multiplies the
        float by `multiplier`. '''
    return lambda x: x * multiplier
