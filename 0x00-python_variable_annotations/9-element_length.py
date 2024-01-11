#!/usr/bin/env python3
'''Annotate the function'''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    ''''''
    return [(i, len(i)) for i in lst]


# print(element_length.__annotations__)
