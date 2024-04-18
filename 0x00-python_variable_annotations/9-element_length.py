#!/usr/bin/env python3
''' Description: Add to the annotations to the below function’s
                 parameters and then return values with just
                 the appropriate types
    Parameters: lst: Iterable[Sequence]
'''

from typing import List, Sequence, Iterable, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''Outputing the list of the tuples, one for just each
        element, of which it consists of the element of
        itself and its length.
    '''
    return [(i, len(i)) for i in lst]
