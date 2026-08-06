from typing import List, Any


def find_duplicates(lst: List[Any]) -> List[Any]:
    """
    Finds and returns all duplicate elements in a list.

    Each duplicate element is returned only once in the result.

    Args:
        lst (List[Any]): The input list.

    Returns:
        List[Any]: A list of unique duplicate elements.
    """
    # Guard case: if list is empty or has only 1 element, no duplicates are possible.
    if len(lst) < 2:
        return []

    seen = set()
    duplicates = set()

    for item in lst:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)

    return list(duplicates)


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([1, 2, 3, 2, 4, 5, 1, 2], [1, 2]),
        ([1, 2, 3, 4, 5], []),
        (["apple", "banana", "apple", "cherry", "banana"], ["apple", "banana"]),
        ([], []),
        ([9], [])
    ]

    for i, (lst, expected) in enumerate(test_cases):
        result = find_duplicates(lst)
        # Convert to sets for order-independent comparison
        assert set(result) == set(expected), f"Test {i+1} failed: expected {expected}, got {result}"
        print(f"Test {i+1} passed: {lst} -> {result}")
