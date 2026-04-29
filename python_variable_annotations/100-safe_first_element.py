#!/usr/bin/env python3
"""
This module augments the following code
with the correct duck-typed annotations
"""

from typing import Sequence, Any, Optional


def safe_first_element(lst):
    """Returns the first element of lst if it exists, otherwise None."""
    if lst:
        return lst[0]
    else:
        return None
