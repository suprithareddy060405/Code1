# Notes - Day 012: Find the Second Largest Number in a List

## Concepts Learned
- **Single-Pass Tracking:** Finding extreme values (largest, second largest, smallest, etc.) can often be done in a single pass $O(N)$ with constant $O(1)$ extra space by maintaining multiple state variables and updating them conditionally.
- **Handling Infinites:** Python's `float('-inf')` is highly useful for initializing variables that represent the minimum possible values, allowing comparison against any integer value.

## Common Mistakes
- **Sorting First:** Sorting the list (`nums.sort()`) and returning `nums[-2]` is a common mistake because it:
  1. Takes $O(N \log N)$ time, which is sub-optimal.
  2. Does not handle duplicate values correctly unless converted to a set first (e.g., `[5, 5, 5]` sorted would return `5` as the second largest, which is the same as the largest).
- **Ignoring Duplicate Maximums:** Failing to verify if a number matches the current `largest` before comparing it to `second_largest`.

## Alternative Solution
Using Python's `set` to remove duplicates, converting back to a list, sorting, and indexing:
```python
def find_second_largest_set(nums):
    unique_nums = list(set(nums))
    if len(unique_nums) < 2:
        return None
    unique_nums.sort()
    return unique_nums[-2]
```
- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(N)$ to store the set/list of unique elements.

## Interview Tips
- Clarify if the "second largest" means the second largest *distinct* element, or if duplicate elements are counted (e.g. in `[10, 10, 8]`, is the second largest 10 or 8?). Most interviewers want the second largest *distinct* element.
- Emphasize the single-pass $O(N)$ solution with $O(1)$ space, as it demonstrates optimization awareness.
