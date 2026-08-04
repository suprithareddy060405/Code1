# Notes - Day 3, Problem 3: Binary Search in Rotated Arrays

## Concepts Learned
1. **Properties of Rotated Sorted Arrays**:
   - No matter where a sorted array is divided/rotated, at least one of the two halves (left or right of the midpoint) will *always* remain sorted.
   - This property allows us to adapt binary search even when the array as a whole is not sorted.
2. **Identifying Sorted Ranges**:
   - `nums[left] <= nums[mid]` guarantees that the range from `left` to `mid` is sorted.
   - Otherwise, the range from `mid` to `right` must be sorted.
3. **Checking Target Bounds**:
   - Once we identify the sorted half, we can easily check if the target lies within its boundaries using simple inequalities (e.g., `nums[left] <= target < nums[mid]`).

## Common Mistakes
- **Incorrect Bound Checks**: Using `<` instead of `<=` when checking sorted portions or checking target ranges. For example, if `left == mid` (when there are 1 or 2 elements), `nums[left] <= nums[mid]` must be true.
- **Deducing sorted side incorrectly**: Assuming that if the left side is not sorted, the right side is not sorted either. In a rotated sorted array with distinct values, exactly one side is always sorted (or both, if not rotated).
- **Infinite Loop**: Forgetting to update `left = mid + 1` or `right = mid - 1` properly, causing `left <= right` to remain true indefinitely.

## Alternative Solution
### Finding Pivot First
Another way to solve this is to first find the pivot index (the index of the minimum element in the array) using a modified binary search, and then perform a standard binary search on either the left or right sorted sub-array.
```python
def find_min_index(nums: list[int]) -> int:
    left, right = 0, len(nums) - 1
    while left < right:
        mid = (left + right) // 2
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    return left

def search_alternative(nums: list[int], target: int) -> int:
    if not nums:
        return -1
    pivot = find_min_index(nums)
    # Target is in the right sorted portion
    if nums[pivot] <= target <= nums[-1]:
        left, right = pivot, len(nums) - 1
    # Target is in the left sorted portion
    else:
        left, right = 0, pivot - 1
        
    # Standard Binary Search
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```
- **Time Complexity:** $O(\log n)$ (one binary search to find pivot, another to find target).
- **Space Complexity:** $O(1)$.

## Interview Tips
- **Ask about duplicate values**: This problem assumes distinct values. If duplicates are allowed (e.g. `[1, 0, 1, 1, 1]`), we cannot determine which half is sorted in $O(1)$ time if `nums[left] == nums[mid] == nums[right]`. In that case, the time complexity degrades to $O(n)$ in the worst case (e.g. LeetCode 81: Search in Rotated Sorted Array II).
- **Trace a small example**: During the interview, walk through an example where the pivot is on the left, and another where it's on the right, to show you understand both conditions.
