#!/usr/bin/env python3
'''
    Description: By using the parameters & then to return values,
    and to add type annotations just to the function
    Parameters: T - a TypeVar with value '~T'
'''

from typing import Mapping, Union, Any, TypeVar

T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    ''' Outputing the dct[key] if it alcually exists,
        otherwise just return `default`. '''
    if key in dct:
        return dct[key]
    else:
        return default
