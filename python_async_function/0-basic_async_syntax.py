#!/usr/bin/env python3
"""This module writes an asynchronous coroutine that takes in an integer argument """
import asyncio
import random


async def wait_random(max_delay: int = 10):
    """Waits for a random delay between 0 and max_delay and return it"""
    delay = random.uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
