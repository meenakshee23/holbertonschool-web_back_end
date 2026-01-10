#!/usr/bin/env python3
"""This module takes the code from wait_n and
alter it into a new function task_wait_n"""
import asyncio
from typing import List
wait_random = __import__('3-tasks').wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_random n times and returns the list of all the delays"""
    results: List[float] = []

    for task in asyncio.as_completed(tasks):
        result = await task
        results.append(result)

    return results
