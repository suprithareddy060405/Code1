# Problem Name: Intersection of Two Arrays

## Problem Statement
Given two integer arrays `nums1` and `nums2`, return an array of their intersection. Each element in the result must be unique and you may return the result in any order.

## Sample Input
```python
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
```

## Sample Output
```python
[2]
```

## Explanation
The only common element between both arrays is `2`. Since we only return unique elements, the result is `[2]`.

Another example:
`nums1 = [4, 9, 5]`, `nums2 = [9, 4, 9, 8, 4]`
Output: `[9, 4]` (or `[4, 9]`)

---

## Approach
We can use Python's built-in `set` data structure to solve this problem efficiently in $O(N + M)$ time.
1. Convert `nums1` to a set. This removes duplicates from `nums1` and allows $O(1)$ average time lookups.
2. Initialize an empty list or set for the result.
3. Iterate through `nums2`, and if an element exists in the set of `nums1`, add it to the result set (to ensure uniqueness).
4. Return the result as a list.

Alternatively, we can use the set intersection operator `&` in Python: `list(set(nums1) & set(nums2))`.

## Time Complexity
- **Time Complexity:** $O(N + M)$ where $N$ is the length of `nums1` and $M$ is the length of `nums2`. Converting arrays to sets takes $O(N)$ and $O(M)$ time respectively, and intersection of sets of size $N$ and $M$ takes $O(\min(N, M))$ average time.

## Space Complexity
- **Space Complexity:** $O(N + M)$ to store the sets in memory.
