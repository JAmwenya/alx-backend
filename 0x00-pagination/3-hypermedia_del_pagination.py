#!/usr/bin/env python3
"""
Deletion-resilient hypermedia pagination.
"""

from typing import Dict, List
from 2-hypermedia_pagination import Server


class Server(Server):
    """Extended Server class to handle deletion-resilient pagination."""

    def indexed_dataset(self) -> Dict[int, List]:
        """
        Dataset indexed by sorting position, starting at 0.
        """
        if self.__indexed_dataset is None:
            dataset = self.dataset()
            self.__indexed_dataset = {i: dataset[i] for i in range(len(dataset))}
        return self.__indexed_dataset

    def get_hyper_index(self, index: int = 0, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with pagination data that is resilient to deletions.
        """
        assert isinstance(index, int) and 0 <= index < len(self.indexed_dataset())

        data = []
        next_index = index
        current_size = 0

        while current_size < page_size and next_index < len(self.indexed_dataset()):
            if next_index in self.indexed_dataset():
                data.append(self.indexed_dataset()[next_index])
                current_size += 1
            next_index += 1

        return {
            "index": index,
            "data": data,
            "page_size": len(data),
            "next_index": next_index
        }
