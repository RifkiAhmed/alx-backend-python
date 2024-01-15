#!/usr/bin/env python3
'''Measure the runtime for an asynchronous coroutines function'''
import asyncio
import time

wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(n: int, max_delay: int) -> float:
    '''Measure the runtime for wait_n() asynchronous coroutines function'''
    start_at: float = time.time()
    asyncio.run(wait_n(n, max_delay))
    end_at = time.time() - start_at
    return end_at / n

# n = 5
# max_delay = 9

# print(measure_time(n, max_delay))
