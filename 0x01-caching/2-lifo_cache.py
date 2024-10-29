#!/usr/bin/python3
""" LIFO caching module
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """class to implement LIFOCache"""
    def __init__(self):
        """child class constructor"""
        super().__init__()

    def put(self, key, item):
        """method put"""
        if key is None or item is None:
            return
        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            key_list = list(self.cache_data.keys())
            l_key = key_list[-1]
            print('DISCARD: {}'.format(l_key))
            del self.cache_data[l_key]

        self.cache_data[key] = item

    def get(self, key):
        """method get"""
        if key is None or self.cache_data.get(key) is None:
            return
        return self.cache_data[key]
