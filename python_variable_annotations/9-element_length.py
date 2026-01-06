#!/usr/bin/env python3
"""This module annotates the function parameters"""


from typing import Iterable, Sequence, List, Tuple


def element_length(lst):
    """Return values with the appropriate types"""
    return [(i, len(i)) for i in lst]
