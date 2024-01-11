#!/usr/bin/env python3
'''Annotate the parameters and the return values of the given function'''
from typing import Any, Sequence, Union


# The types of the elements of the input are not know
def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    '''Return the first element of the iterable lst else None'''
    if lst:
        return lst[0]
    else:
        return None

# print(safe_first_element.__annotations__)
