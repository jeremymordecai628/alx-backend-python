#!/usr/bin/env python3
"""
Module: 0-async_generator
This module defines the async_generator coroutine that yields random numbers asynchronously.
"""

import asyncio
import random

async def async_generator():
    """
    Asynchronously yield random numbers between 0 and 10.
    
    Yields:
        float: A random floating-point number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
