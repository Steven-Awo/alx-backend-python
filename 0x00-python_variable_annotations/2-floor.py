#!/usr/bin/env python3
''' Description:takes in a float n as an argument and then returns
    the floor of the float
    Parameter: x: float
'''


def floor(x: float) -> int:
    ''' Return's the largest int value thats less than or equal to n. '''
    return int(x) if x >= 0 else int(x) - 1
