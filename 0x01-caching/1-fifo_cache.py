#!/usr/bin/env python3
"""
FIFO caching system
"""

from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFO caching system with a limit
    """

    def __init__(self):
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item to the cache (FIFO eviction if needed)
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            self.cache_data[key] = item
            self.order.append(key)

            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                discarded = self.order.pop(0)
                del self.cache_data[discarded]
                print(f"DISCARD: {discarded}")

    def get(self, key):
        """
        Get an item from the cache
        """
        return self.cache_data.get(key, None)
