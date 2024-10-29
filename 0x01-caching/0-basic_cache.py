#!/usr/bin/python3
""" BaseCaching module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """class to implement BaseCache"""
    def put(self, key, item):
        """method put"""
        if key is None or item is None:
            return
        self.cache_data[key] = item

    def get(self, key):
        """method get"""
        if key is None or self.cache_data.get(key) is None:
            return
        return self.cache_data[key]
