#!/usr/bin/python3
""" MRU caching module
"""
from base_caching import BaseCaching
import collections


class MRUCache(BaseCaching):
    """class to implement MRUCache"""
    def __init__(self):
        """child class constructor"""
        super().__init__()
        self.od = collections.OrderedDict()

    def put(self, key, item):
        """method put"""
        if key is None or item is None:
            return
        if key in self.cache_data:
            self.cache_data[key] = item
            self.od[key] = item
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                l_key = list(self.od.keys())[0]
                del self.cache_data[l_key]
                del self.od[l_key]
                print('DISCARD: {}'.format(l_key))

            self.cache_data[key] = item
            self.od[key] = item

        self.od.move_to_end(key, last=False)

    def get(self, key):
        """method get"""
        if key is None or self.cache_data.get(key) is None:
            return
        self.od.move_to_end(key, last=False)
        return self.cache_data[key]
