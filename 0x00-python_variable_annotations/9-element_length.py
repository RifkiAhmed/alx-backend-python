#!/usr/bin/env python3
'''Annotate the parameters and the return values of the given function'''
from typing import Iterable, List, Tuple, Sequence


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    '''return a list of tuples of each ele of the iterable lst and its len'''
    return [(i, len(i)) for i in lst]


# print(element_length.__annotations__)
