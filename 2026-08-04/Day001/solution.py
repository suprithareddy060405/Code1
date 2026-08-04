"""
Day 3: Problem 1 - Intersection of Two Arrays (Sets)
Language: Python 3
"""

from typing import List


def intersection(nums1: List[int], nums2: List[int]) -> List[int]:
    """
    Finds the intersection of two integer arrays. Each element in the result
    must be unique, and the result can be returned in any order.

    Time Complexity: O(N + M) where N is len(nums1) and M is len(nums2).
    Space Complexity: O(N + M) to store set representations.
    """
    # Convert both lists to sets to get unique elements and O(1) lookups
    set1 = set(nums1)
    set2 = set(nums2)

    # Use set intersection to find common elements, then convert back to list
    return list(set1.intersection(set2))


if __name__ == "__main__":
    # Sample and Edge Test Cases
    test_cases = [
        # Normal case
        (([1, 2, 2, 1], [2, 2]), [2]),
        # Multiple intersections
        (([4, 9, 5], [9, 4, 9, 8, 4]), [4, 9]),
        # No intersection
        (([1, 2, 3], [4, 5, 6]), []),
        # Empty arrays (Edge cases)
        (([], [1, 2]), []),
        (([1, 2], []), []),
        (([], []), []),
        # Identical arrays
        (([1, 1, 1], [1, 1]), [1]),
    ]

    for i, ((arr1, arr2), expected) in enumerate(test_cases, 1):
        result = intersection(arr1, arr2)
        # Since order of result doesn't matter, we compare sorted lists or sets
        assert set(result) == set(expected), (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )
        print(f"Test case {i} passed: intersection({arr1}, {arr2}) -> {result}")

    print("All sample test cases executed successfully!")
