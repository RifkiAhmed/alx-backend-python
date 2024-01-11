#!/usr/bin/env python3
'''Floor of a number using type-annotated function'''
import math


def floor(n: float) -> int:
    '''Return the floor of the number n'''
    return math.floor(n)


# ans = floor(3.14)

# print(ans == math.floor(3.14))
# print(floor.__annotations__)
# print("floor(3.14) returns {}, which is a {}".format(ans, type(ans)))
