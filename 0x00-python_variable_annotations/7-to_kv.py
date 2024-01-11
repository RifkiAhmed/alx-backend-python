#!/usr/bin/env python3
'''Return a tuple using a type-annotated function'''
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    '''Return a tuple(k, v)'''
    return (k, v * v)

# print(to_kv.__annotations__)
# print(to_kv("eggs", 3))
# print(to_kv("school", 0.02))
