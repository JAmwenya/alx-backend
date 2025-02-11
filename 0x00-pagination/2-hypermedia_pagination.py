#!/usr/bin/env python3
"""
Hypermedia pagination implementation.
"""

from math import ceil
from typing import Dict
from 1-simple_pagination import Server


class Server(Server):
    """Extended Server class to include hypermedia pagination."""

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary with hypermedia pagination data.
        """
        data = self.get_page(page, page_size)
        total_pages = ceil(len(self.dataset()) / page_size)

        return {
            "page_size": len(data),
            "page": page,
            "data": data,
            "next_page": page + 1 if page < total_pages else None,
            "prev_page": page - 1 if page > 1 else None,
            "total_pages": total_pages
        }
