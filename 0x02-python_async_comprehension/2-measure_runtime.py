#!/usr/bin/env python3
"""Run time for four parallel comprehensions"""
import asyncio
import time
from typing import List
module = __import__('1-async_comprehension')
async_comprehension = module.async_comprehension


async def measure_runtime() -> float:
    """Measure total runtime"""
    start_time = time.time()
    await asyncio.gather(*(async_comprehension() for _ in range(4)))
    end_time = time.time()
    return end_time - start_time
