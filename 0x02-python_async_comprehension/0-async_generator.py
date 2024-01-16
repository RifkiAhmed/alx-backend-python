#!/usr/bin/env python3
'''Asynchronous Generator'''
import asyncio
from typing import AsyncGenerator


async def async_generator() -> AsyncGenerator[float, None]:
    '''
    Asynchronous generator function that yields random numbers
    between 0 and 10 with a 1s delay between each yield
    '''
    import random

    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)


# Test case:
#
# async def print_yielded_values():
#     result = []
#     async for i in async_generator():
#         result.append(i)
#     print(result)
# asyncio.run(print_yielded_values())
