#!/usr/bin/python3
""" LRU caching module
"""
from base_caching import BaseCaching
import collections


class LRUCache(BaseCaching):
    """class to implement LRUCache"""
    def __init__(self):
        """child class constructor"""
        super().__init__()

    def put(self, key, item):
        """method put"""
        if key is None or item is None:
            return
        if len(self.od) >= BaseCaching.MAX_ITEMS:
            
            if key not in self.od.keys():
                l_key = list(self.od.keys())[0]
                del self.od[l_key]
                print('DISCARD: {}'.format(l_key))
            else:
                self.od[key] = item
                self.od.move_to_end(key)
                return

        self.od[key] = item
 
    def get(self, key):
        """method get"""
        if key is None or self.od.get(key) is None:
            return
        self.od.move_to_end(key)
        return self.od[key]
