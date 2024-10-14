#!/usr/bin/env python3
"""
This module contains the measure_time function that calculates
the average runtime of the wait_n coroutine.
"""

import time
import asyncio

async_comprehension = __import__('1-async_comprehension').async_comprehension

async def measure_runtime() -> float:
    """
    Measure the total runtime of executing async_comprehension
    four times in parallel.
    """
    start_time = time.perf_counter()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.perf_counter()
    return end_time - start_time
