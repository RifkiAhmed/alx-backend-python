#!/usr/bin/env python3
'''Validate the following piece of code and apply necessary changes:

def zoom_array(lst: Tuple, factor: int = 2) -> Tuple:
    zoomed_in: Tuple = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = [12, 72, 91]

zoom_2x = zoom_array(array)

zoom_3x = zoom_array(array, 3.0)
'''
from typing import Tuple, List


def zoom_array(lst: Tuple, factor: int = 2) -> List:
    '''Return a new list by repeating each item in the lst factor times'''
    zoomed_in: List = [
        item for item in lst
        for i in range(factor)
    ]
    return zoomed_in


array = (12, 72, 91)

zoom_2x = zoom_array(array)
# print(zoom_2x)
zoom_3x = zoom_array(array, 3)
# print(zoom_3x)
# print(zoom_array.__annotations__)
