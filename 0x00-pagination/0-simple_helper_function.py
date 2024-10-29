#!/usr/bin/env python3
"""script for index range"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that compute problem"""
    offset = (page - 1) * page_size
    endidx = offset + page_size

    return (offset, endidx)
