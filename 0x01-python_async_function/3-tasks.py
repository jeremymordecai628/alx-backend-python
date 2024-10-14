#!/usr/bin/env python3
"""
This module contains a function task_wait_random that creates an asyncio.Task
from the wait_random coroutine using __import__ for dynamic import.
"""

import asyncio

# Dynamically import wait_random from the file '0-basic_async_syntax.py'
wait_random = __import__('0-basic_async_syntax').wait_random

def task_wait_random(max_delay: int) -> asyncio.Task:
    """
    Creates and returns an asyncio.Task that runs the wait_random coroutine.

    :param max_delay: Maximum delay for the wait_random coroutine
    :return: asyncio.Task
    """
    return asyncio.create_task(wait_random(max_delay))
