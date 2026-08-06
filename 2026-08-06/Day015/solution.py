from typing import List, Any


def linear_search(lst: List[Any], target: Any) -> int:
    """
    Performs a linear search to find the index of target in lst.

    Constraints: Does not use Python's built-in 'in' or '.index()'.

    Args:
        lst (List[Any]): The list to search.
        target (Any): The value to search for.

    Returns:
        int: The 0-based index of the target if found, otherwise -1.
    """
    # Guard case: if list is empty, search fails immediately
    if not lst:
        return -1

    for idx, item in enumerate(lst):
        # Perform comparison
        if item == target:
            return idx

    # If loop completes, target was not found
    return -1


if __name__ == "__main__":
    # Test cases
    test_cases = [
        (([4, 2, 7, 1, 9], 7), 2),
        (([4, 2, 7, 1, 9], 5), -1),
        ((["apple", "orange", "grape"], "grape"), 2),
        (([], 10), -1),
        (([10], 10), 0)
    ]

    for i, ((lst, target), expected) in enumerate(test_cases):
        result = linear_search(lst, target)
        assert result == expected, f"Test {i+1} failed: expected {expected}, got {result}"
        print(f"Test {i+1} passed: search for {target} in {lst} -> index {result}")
