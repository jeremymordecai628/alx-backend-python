#!/usr/bin/env python3
"""
Module: 1-async_comprehension
This module defines the async_comprehension coroutine that collects random numbers using async comprehension.
"""

async def async_comprehension():
    """
    Collect 10 random numbers from async_generator using async comprehension.
    
    Returns:
        list: A list of 10 random floating-point numbers between 0 and 10.
    """
    async_generator = __import__('0-async_generator').async_generator
    return [i async for i in async_generator()]
