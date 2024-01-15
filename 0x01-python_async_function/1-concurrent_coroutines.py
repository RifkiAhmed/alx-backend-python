#!/usr/bin/env python3
'''Asynchronous coroutines'''
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynchronous coroutines that waits for a random delays'''
    delays = []
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay = await task
        delays.append(delay)
    return delays

# print(asyncio.run(wait_n(5, 5)))
# print(asyncio.run(wait_n(10, 7)))
# print(asyncio.run(wait_n(10, 0)))
