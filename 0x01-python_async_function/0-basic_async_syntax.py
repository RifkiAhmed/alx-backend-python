#!/usr/bin/env python3
'''Asynchronous coroutine'''
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    '''Asynchronous coroutine that waits for a random delay and returns it'''
    import random

    delay: int = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay

# print(asyncio.run(wait_random()))
# print(asyncio.run(wait_random(5)))
# print(asyncio.run(wait_random(15)))
