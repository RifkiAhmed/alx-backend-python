#!/usr/bin/env python3
'''Asynchronous coroutine that uses an asynchronous comprehensing'''
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    '''
    Asynchronous coroutine that collects numbers using an async comprehensing
    over async_generator
    '''
    return [n async for n in async_generator()]


# async def main():
#     print(await async_comprehension())
# asyncio.run(main())
