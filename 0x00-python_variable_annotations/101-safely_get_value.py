#!/usr/bin/env python3

from typing import Dict, TypeVar, Optional

# Define type variables for the key and value types
K = TypeVar('K')  # Type variable for the key
V = TypeVar('V')  # Type variable for the value

def safely_get_value(dct: Dict[K, V], key: K, default: Optional[V] = None) -> Optional[V]:
    if key in dct:
        return dct[key]
    else:
        return default

