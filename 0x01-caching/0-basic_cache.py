#!/usr/bin/env python3
"""
Basic caching system
"""

from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    A caching system with no limit (basic dictionary)
    """

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
