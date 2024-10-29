#!/usr/bin/env python3
"""script for hypermedia pagination"""
from typing import Tuple
import csv
import math
from typing import List


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """function that compute problem"""
    offset = (page - 1) * page_size
    endidx = offset + page_size

    return (offset, endidx)


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """method get_page"""
        if not isinstance(page, int) or page <= 0:
            raise AssertionError
        if not isinstance(page_size, int) or page_size <= 0:
            raise AssertionError

        start, end = index_range(page, page_size)
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
        start += 1
        self.__dataset = dataset[start:end + 1]
        return self.__dataset

    def get_hyper(self, page: int = 1, page_size: int = 10) -> dict:
        """method for hypermedia pagination"""
        with open(self.DATA_FILE) as f:
            reader = csv.reader(f)
            dataset = [row for row in reader]
        offset = (page - 1) * page_size
        endidx = offset + page_size

        data = self.get_page(page, page_size)

        if endidx >= len(dataset):
            next_page = None

        else:
            next_page = page + 1
        if page <= 1:
            prev_page = None
        else:
            prev_page = page - 1

        total_page = (len(dataset) + page_size - 1) // page_size
        if not next_page:
            page_size = 0

        _dict = {
            'page_size': page_size,
            'page': page,
            'data': data,
            'next_page': next_page,
            'prev_page': prev_page,
            'total_page': total_page
        }
        return _dict
