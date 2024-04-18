#!/usr/bin/env python3
''' Description: accepting the list called mxd_lst of just floats
    and integers and then returns their summation as a float.
    Parameters: mxd_lst: List[Union[int, float]]
'''

from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    ''' Outputing the total sum of the elements in mxd_list. '''
    return sum(mxd_lst)
