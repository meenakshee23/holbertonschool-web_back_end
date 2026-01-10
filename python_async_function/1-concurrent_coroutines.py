#!/usr/bin/env python3
"""
This module  writes an async routine called
wait_n that takes in 2 int arguments
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Runs wait_random n times and returns the list of all the delays"""
    tasks = [asyncio.create_task(wait_random(max_delay)) for _ in range(n)]
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
