#!/usr/bin/env python3
"""
This module contains the asynchronous coroutine wait_random,
which waits for a random delay between 0 and max_delay seconds.
"""
import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """
    Asynchronous coroutine that waits for a random delay between
    0 and max_delay (inclusive) seconds, then returns the delay.

    :param max_delay: Maximum value for the random delay (default 10)
    :return: The actual delay time in seconds
    """
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
