#!/usr/bin/env python3
''' Description: this takes in a float 'n' as argument and the returns the floor's float
    Parameter: n: float
'''


def floor(n: float) -> int:
    ''' Returning largest int value less than or equal to n. '''
    return int(n) if n >= 0 else int(n) - 1
