#!/usr/bin/env python3
''' Description:takes in a float n as an argument and then returns
    the floor of the float
    Parameter: numb: float
'''


def floor(nunb: float) -> int:
    ''' Return's the largest int value thats less than or equal to n. '''
    return int(numb) if numb >= 0 else int(numb) - 1
