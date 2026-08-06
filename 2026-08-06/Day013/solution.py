from typing import Dict, Any


def merge_dictionaries(dict1: Dict[Any, Any], dict2: Dict[Any, Any]) -> Dict[Any, Any]:
    """
    Merges two dictionaries. If a key is present in both, the value from
    dict2 overwrites the value from dict1.

    This function does NOT modify the input dictionaries.

    Args:
        dict1 (Dict[Any, Any]): The first dictionary.
        dict2 (Dict[Any, Any]): The second dictionary.

    Returns:
        Dict[Any, Any]: A new dictionary containing the merged result.
    """
    # Guard clauses to handle empty inputs
    if dict1 is None:
        return dict2.copy() if dict2 is not None else {}
    if dict2 is None:
        return dict1.copy()

    # Python 3.9+ Dictionary Merge Operator
    return dict1 | dict2


if __name__ == "__main__":
    # Test cases
    d1 = {'a': 1, 'b': 2}
    d2 = {'b': 99, 'c': 4}
    expected = {'a': 1, 'b': 99, 'c': 4}

    result = merge_dictionaries(d1, d2)
    assert result == expected, f"Expected {expected}, got {result}"
    # Verify non-mutation
    assert d1 == {'a': 1, 'b': 2}, "dict1 was mutated!"
    assert d2 == {'b': 99, 'c': 4}, "dict2 was mutated!"
    print("Test 1 passed: Overlapping keys merged and original dicts not mutated.")

    # Empty dictionary test
    result_empty = merge_dictionaries({}, {'x': 10})
    assert result_empty == {'x': 10}, f"Expected {{'x': 10}}, got {result_empty}"
    print("Test 2 passed: Merging with empty dictionary.")
