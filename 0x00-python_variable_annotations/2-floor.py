#!/usr/bin/env python3
''' Description:this takes in a float 'n' as argument and the returns the
    floor's float
    Parameter: n: float
'''



def floor(x: float) -> int:
    ''' Returning the largest int value less than
        or equal to n. '''
    return int(x) if x >= 0 else int(x) - 1
