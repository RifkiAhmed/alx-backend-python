#!/usr/bin/env python3
'''Sum of list elements of type float using type-annotated function'''
from typing import List


def sum_list(input_list: List[float]) -> float:
    '''Return sum of input_list elements'''
    return sum(input_list)


# floats = [3.14, 1.11, 2.22]
# floats_sum = sum_list(floats)
# print(floats_sum == sum(floats))
# print(sum_list.__annotations__)
# print("sum_list(floats) returns {} which is a {}".format(
#     floats_sum, type(floats_sum)))
