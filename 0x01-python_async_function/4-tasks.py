#!/usr/bin/env python3
"""
This module contains the implementation of the async coroutine task_wait_n
that spawns task_wait_random n times and returns a list of delays in ascending order.
"""

import asyncio
from typing import List
from heapq import heappush, heappop

# Dynamically import task_wait_random using __import__
task_wait_random = __import__('3-tasks').task_wait_random

async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns task_wait_random n times with the specified max_delay and returns
    a list of the delays in ascending order without using sort().

    :param n: Number of times to spawn task_wait_random
    :param max_delay: Maximum delay value to pass to task_wait_random
    :return: List of delay times in ascending order
    """
    delays = []

    # Create and execute all task_wait_random tasks concurrently
    tasks = [task_wait_random(max_delay) for _ in range(n)]

    # Use asyncio.as_completed to get results as they finish
    for task in asyncio.as_completed(tasks):
        delay = await task
        heappush(delays, delay)

    # Extract the delays in ascending order using a heap
    ordered_delays = [heappop(delays) for _ in range(n)]
    return ordered_delays
