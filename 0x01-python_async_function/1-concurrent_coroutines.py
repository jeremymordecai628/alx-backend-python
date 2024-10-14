#!/usr/bin/env python3
"""
This module contains the implementation of the async coroutine wait_n
that spawns wait_random n times and returns a list of delays in ascending order.
"""

import asyncio
from typing import List
from heapq import heappush, heappop



async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    Spawns wait_random n times with the specified max_delay and returns a list
    of the delays in ascending order without using sort().

    :param n: Number of times to spawn wait_random
    :param max_delay: Maximum delay value to pass to wait_random
    :return: List of delay times in ascending order
    """
    delays = []
    
    # Create and execute all wait_random coroutines concurrently
    coroutines = [wait_random(max_delay) for _ in range(n)]
    
    # Use asyncio.as_completed to get results as they finish
    for result in asyncio.as_completed(coroutines):
        delay = await result
        heappush(delays, delay)

    # Extract the delays in ascending order using a heap
    ordered_delays = [heappop(delays) for _ in range(n)]
    return ordered_delays
