#!/usr/bin/env python3
'''Sum of a list of integers and floats using a typs-annotated function'''
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    '''Return sum of mxd_lst elements'''
    return sum(mxd_lst)


# print(sum_mixed_list.__annotations__)
# mixed = [5, 4, 3.14, 666, 0.99]
# ans = sum_mixed_list(mixed)
# print(ans == sum(mixed))
# print("sum_mixed_list(mixed) returns {} which is a {}".format(ans, type(ans)))
