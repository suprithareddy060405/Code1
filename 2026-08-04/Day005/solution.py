"""
Day 3: Problem 5 - Merge Intervals (Sorting)
Language: Python 3
"""

from typing import List


def merge(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merges all overlapping intervals.

    Time Complexity: O(N log N) where N is the number of intervals.
    Space Complexity: O(N) to store the result.
    """
    if not intervals:
        return []

    # Sort the intervals based on the start coordinate
    intervals.sort(key=lambda x: x[0])

    merged = []
    for interval in intervals:
        # If merged is empty or no overlap, append the interval
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            # Overlap exists; merge by updating the end time of the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        # Normal case
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
        # Overlapping boundary
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
        ),
        # Fully nested intervals
        (
            [[1, 10], [2, 3], [4, 5]],
            [[1, 10]],
        ),
        # Single interval
        (
            [[1, 5]],
            [[1, 5]],
        ),
        # Empty input list
        (
            [],
            [],
        ),
        # All overlapping
        (
            [[1, 4], [2, 5], [3, 6]],
            [[1, 6]],
        ),
        # Unsorted intervals as input
        (
            [[15, 18], [2, 6], [1, 3], [8, 10]],
            [[1, 6], [8, 10], [15, 18]],
        ),
    ]

    for i, (input_intervals, expected) in enumerate(test_cases, 1):
        # We make a copy because merge() sorts in-place which modifies the test case input
        result = merge([list(item) for item in input_intervals])
        assert result == expected, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )
        print(f"Test case {i} passed: merge({input_intervals}) -> {result}")

    print("All sample test cases executed successfully!")
