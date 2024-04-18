#!/usr/bin/env python3
''' Description: accepts the list called input_list of just floats
    as an argument and returns their summation as a float.
    Arguments: input_list: List[float]
'''

from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Outputs the total sum of all the elements in input_list. '''
    return sum(input_list)
