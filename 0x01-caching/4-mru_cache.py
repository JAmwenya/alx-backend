#!/usr/bin/env python3
"""
MRU caching system
"""

from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRU caching system with a limit
    """

    def __init__(self):
        super().__init__()
        self.last = None

    def put(self, key, item):
        """
        Add an item to the cache (MRU eviction if needed)
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.cache_data.pop(key)
            self.cache_data[key] = item
            self.last = key

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.last
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")
                self.last = next(reversed(self.cache_data), None)

    def get(self, key):
        """
        Get an item from the cache
        """
        if key in self.cache_data:
            self.last = key
            return self.cache_data[key]
        return None
