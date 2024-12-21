#!/usr/bin/env python3
"""
LIFO caching system
"""

from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFO caching system with a limit
    """

    def __init__(self):
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Add an item to the cache (LIFO eviction if needed)
        """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                if self.last is not None:
                    del self.cache_data[self.last]
                    print(f"DISCARD: {self.last}")
            self.last = key

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
