#!/usr/bin/env python3
'''Asynchronous coroutines'''
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    '''Asynchronous coroutines that waits for a random delays'''
    delays: List[float] = []
    tasks: List[asyncio.Task] = [task_wait_random(max_delay) for _ in range(n)]
    for task in asyncio.as_completed(tasks):
        delay: float = await task
        delays.append(delay)
    return delays

# Example
# n = 5
# max_delay = 6
# print(asyncio.run(task_wait_n(n, max_delay)))
