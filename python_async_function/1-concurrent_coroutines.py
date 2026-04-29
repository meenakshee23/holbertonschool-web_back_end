#!/usr/bin/env python3
"""
This module Import wait_random from the previous
python file that you've written and
write an async routine called wait_n
that takes in 2 int arguments (in this order)
"""

import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Return the list of all the delays (float values)"""
    tasks = [wait_random(max_delay) for _ in range(n)]
    delays = []

    for completed in asyncio.as_completed(tasks):
        delay = await completed
        delays.append(delay)

    return delays
