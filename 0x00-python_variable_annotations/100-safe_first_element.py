#!/usr/bin/env python3
''' Description: To build upon just the following code with the corrects
                 duck-typed's annotations
    Parameters: lst: Sequence[Any]
'''

from typing import Any, Sequence, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    ''' Outputing the first element thats of lst if there's
        any, otherwise None. '''
    if lst:
        return lst[0]
    else:
        return None
