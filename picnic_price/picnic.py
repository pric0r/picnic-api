"""Wrapper functions for picnic API."""

from typing import List

from picnic_price.schema import Item

from python_picnic_api import PicnicAPI


def search_items(picnic_api: PicnicAPI, term: str) -> List[Item]:
    result = picnic_api.search(term=term)
    items_dict = result[0]["items"]
    items = [
        Item(**item)
        for item in items_dict
        if ("name" in item) and ("unit_quantity_sub" in item)
    ]
    return items
