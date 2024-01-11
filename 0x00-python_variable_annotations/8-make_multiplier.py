#!/usr/bin/env python3
''''''
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    def f_multiplier(n: float) -> float:
        return multiplier * n
    return f_multiplier

# print(make_multiplier.__annotations__)
# fun = make_multiplier(2.22)
# print("{}".format(fun(2.22)))
