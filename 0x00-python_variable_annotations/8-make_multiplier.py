#!/usr/bin/env python3
'''Make a callable'''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    '''Return a callable (function) that multiply a number by multiplier'''
    def f_multiplier(n: float) -> float:
        return multiplier * n
    return f_multiplier

# print(make_multiplier.__annotations__)
# fun = make_multiplier(2.22)
# print("{}".format(fun(2.22)))
