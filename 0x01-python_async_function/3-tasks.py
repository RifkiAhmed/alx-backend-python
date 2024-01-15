#!/usr/bin/env python3
'''Asynchronous task'''
import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int) -> asyncio.Task:
    '''Create an asynchronous task'''
    return asyncio.create_task(wait_random(max_delay))

# Example
#
# async def test(max_delay: int) -> float:
#     task = task_wait_random(max_delay)
#     await task
#     print(task.__class__)
# asyncio.run(test(5)) # -> <class '_asyncio.Task'>
