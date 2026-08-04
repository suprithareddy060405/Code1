"""
Day 3: Problem 3 - Search in Rotated Sorted Array (Searching)
Language: Python 3
"""

from typing import List


def search(nums: List[int], target: int) -> int:
    """
    Searches for a target in a rotated sorted array.
    Returns the index if found, else -1.

    Time Complexity: O(log n)
    Space Complexity: O(1)
    """
    if not nums:
        return -1

    left = 0
    right = len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # Check if the left portion is sorted
        if nums[left] <= nums[mid]:
            # Target lies within the sorted left portion
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        # Otherwise, the right portion must be sorted
        else:
            # Target lies within the sorted right portion
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        # Normal rotated array, target in left sorted part
        (([4, 5, 6, 7, 0, 1, 2], 5), 1),
        # Normal rotated array, target in right sorted part
        (([4, 5, 6, 7, 0, 1, 2], 0), 4),
        # Target not present
        (([4, 5, 6, 7, 0, 1, 2], 3), -1),
        # Single element array - found
        (([1], 1), 0),
        # Single element array - not found
        (([1], 0), -1),
        # Not rotated (fully sorted) array
        (([1, 3, 5], 3), 1),
        (([1, 3, 5], 1), 0),
        (([1, 3, 5], 5), 2),
        # Empty array edge case
        (([], 5), -1),
    ]

    for i, ((array, tgt), expected) in enumerate(test_cases, 1):
        result = search(array, tgt)
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )
        print(f"Test case {i} passed: search({array}, {tgt}) -> {result}")

    print("All sample test cases executed successfully!")
