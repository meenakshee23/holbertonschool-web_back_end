#!/usr/bin/env python3
"""This module writes a type-annotated function to_kv"""


from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Return a tuple where first element is k and second element is v squared as float."""
    return (k, float(v ** 2))
