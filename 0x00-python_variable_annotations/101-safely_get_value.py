#!/usr/bin/env python3
'''Annotate the parameters and the return values of the given function'''
from typing import Any, Mapping, TypeVar, Union
T = TypeVar('T')


def safely_get_value(dct: Mapping,
                     key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    '''Return the key value from the dct else return default'''
    if key in dct:
        return dct[key]
    else:
        return default

# annotations = safely_get_value.__annotations__

# print("Here's what the mappings should look like")
# for k, v in annotations.items():
#     print( ("{}: {}".format(k, v)))
