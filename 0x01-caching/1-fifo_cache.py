#!/usr/bin/python3
""" FIFO caching module
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """class to implement FIFOCache"""
    def __init__(self):
        """child class constructor"""
        super().__init__()

    def put(self, key, item):
        """method put"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            f_key = next(iter(self.cache_data))
            print('DISCARD: {}'.format(f_key))
            del self.cache_data[f_key]

        self.cache_data[key] = item

    def get(self, key):
        """method get"""
        if key is None or self.cache_data.get(key) is None:
            return
        return self.cache_data[key]
