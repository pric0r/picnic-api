"""Utility functions."""

import itertools
import json
from pathlib import Path
from typing import List, Tuple

from picnic_price.schema import Item


def credentials_from_file(path: Path) -> Tuple[str, str, str]:
    credentials = json.load(open(path))
    username = credentials["username"]
    password = credentials["password"]
    country_code = credentials["country_code"]
    return username, password, country_code


def filter_cheapest_items(items: List[Item], max_n: int) -> List[Item]:
    items_ascending = sorted(items, key=lambda item: item.eur_per_kg)
    return list(itertools.islice(items_ascending, max_n))
