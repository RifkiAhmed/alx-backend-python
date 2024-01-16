#!/usr/bin/env python3
'''
Asynchronous coroutine that measures the runtime of 4 asynchronous coroutines
executed in parallel
'''
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    '''
    Measure the runtime of 4 asynchronous coroutines executed in parallel
    '''
    import time

    started_at: float = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    return time.time() - started_at


# test code:
#
# async def main():
#     return await(measure_runtime())
#
# print(asyncio.run(main()))
