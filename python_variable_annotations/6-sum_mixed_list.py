#!/usr/bin/env python3
"""This module defines a type-annotated function sum"""


from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Return the sum of a list of integers and floats as a float."""
    total = sum(mxd_lst)
    return float(total)
