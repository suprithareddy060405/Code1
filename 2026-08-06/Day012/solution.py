from typing import List, Optional


def find_second_largest(nums: List[int]) -> Optional[int]:
    """
    Finds the second largest distinct number in a list of integers.

    If the list has fewer than 2 unique numbers, returns None.

    Args:
        nums (List[int]): The list of numbers to search.

    Returns:
        Optional[int]: The second largest distinct number, or None.
    """
    # Guard case: if list is empty or has less than 2 items, we can return early
    if len(nums) < 2:
        return None

    # Track largest and second largest numbers
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            # Shift largest to second largest, update largest
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Update second largest if it's strictly greater and not equal to largest
            second_largest = num

    # Return None if second_largest was never updated from its initial negative infinity
    return second_largest if second_largest != float('-inf') else None


if __name__ == "__main__":
    # Test cases
    test_cases = [
        ([3, 5, 5, 4], 4),
        ([10, 10, 10], None),
        ([12, 35, 1, 10, 34, 1], 34),
        ([10, 5], 5),
        ([5, 10], 5),
        ([1], None),
        ([], None)
    ]

    for i, (lst, expected) in enumerate(test_cases):
        result = find_second_largest(lst)
        assert result == expected, f"Test {i+1} failed for {lst}: expected {expected}, got {result}"
        print(f"Test {i+1} passed: {lst} -> {result}")
