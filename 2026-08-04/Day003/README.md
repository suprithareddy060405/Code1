# Problem Name: Search in Rotated Sorted Array

## Problem Statement
There is an integer array `nums` sorted in ascending order (with distinct values).

Prior to being passed to your function, `nums` is possibly rotated at an unknown pivot index `k` (`1 <= k < nums.length`) such that the resulting array is `[nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]` (0-indexed). For example, `[0, 1, 2, 4, 5, 6, 7]` might be rotated at pivot index `3` and become `[4, 5, 6, 7, 0, 1, 2]`.

Given the array `nums` after the possible rotation and an integer `target`, return the index of `target` if it is in `nums`, or `-1` if it is not in `nums`.

You must write an algorithm with $O(\log n)$ runtime complexity.

## Sample Input
```python
nums = [4, 5, 6, 7, 0, 1, 2]
target = 0
```

## Sample Output
```python
4
```

## Explanation
The value `0` is located at index `4` in the array.

Another example:
`nums = [4, 5, 6, 7, 0, 1, 2]`, `target = 3`
Output: `-1`

---

## Approach
We can use a modified version of **Binary Search**:
1. Initialize two pointers: `left = 0` and `right = len(nums) - 1`.
2. While `left <= right`, calculate the midpoint `mid = (left + right) // 2`.
3. If `nums[mid] == target`, we found the target and return `mid`.
4. Determine which half of the array is sorted (either the left half or the right half):
   - **Left Half is Sorted:** `nums[left] <= nums[mid]`
     - If the target lies within the range of this sorted left half (`nums[left] <= target < nums[mid]`), search in the left half by updating `right = mid - 1`.
     - Otherwise, search in the right half: `left = mid + 1`.
   - **Right Half is Sorted:** `nums[left] > nums[mid]` (implying `nums[mid] <= nums[right]`)
     - If the target lies within the range of this sorted right half (`nums[mid] < target <= nums[right]`), search in the right half by updating `left = mid + 1`.
     - Otherwise, search in the left half: `right = mid - 1`.
5. If the loop ends and we haven't found the target, return `-1`.

## Time Complexity
- **Time Complexity:** $O(\log n)$ because we halve the search space at each step of the binary search.

## Space Complexity
- **Space Complexity:** $O(1)$ auxiliary space as we only use a few pointer variables.
