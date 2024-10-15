#!/usr/bin/env python3
"""
Module: 2-measure_runtime
This module defines the measure_runtime coroutine that runs async_comprehension four times in parallel and measures the total runtime.
"""

import asyncio
import time

async def measure_runtime():
    """
    Execute async_comprehension four times in parallel and measure the total runtime.
    
    Returns:
        float: The total time taken to execute async_comprehension four times.
    """
    async_comprehension = __import__('1-async_comprehension').async_comprehension
    
    start_time = time.perf_counter()
    
    # Run async_comprehension four times in parallel
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    
    end_time = time.perf_counter()
    
    return end_time - start_time
