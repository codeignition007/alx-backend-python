#!/usr/bin/env python3

from typing import List, Any, Union

# The types of the elements of the input are not known
def safe_first_element(lst: List[Any]) -> Union[Any, None]:
    if lst:
        return lst[0]
    else:
        return None

