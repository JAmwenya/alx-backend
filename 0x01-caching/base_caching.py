#!/usr/bin/python3
"""
BaseCaching module
"""


class BaseCaching:
    """
    BaseCaching defines:
      - Constants for the caching system
      - Where the data is stored (a dictionary)
    """

    MAX_ITEMS = 4

    def __init__(self):
        """
        Initialize the cache
        """
        self.cache_data = {}

    def print_cache(self):
        """
        Print the current state of the cache
        """
        print("Current cache:")
        for key in sorted(self.cache_data.keys()):
            print(f"{key}: {self.cache_data[key]}")

    def put(self, key, item):
        """
        Add an item to the cache
        """
        raise NotImplementedError("put must be implemented in your cache class")

    def get(self, key):
        """
        Get an item from the cache by key
        """
        raise NotImplementedError("get must be implemented in your cache class")
