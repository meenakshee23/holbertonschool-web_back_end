#!/usr/bin/env python3
"""This module writes a type-annotated function make_multiplier"""


from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    return lambda x: x * multiplier
