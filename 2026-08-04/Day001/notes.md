# Notes - Day 3, Problem 1: Sets & Intersections

## Concepts Learned
1. **Set Membership and Uniqueness**:
   - Python's `set` is implemented as a hash table, offering $O(1)$ average time complexity for insertions, deletions, and lookups.
   - Using sets is the most straightforward way to eliminate duplicates from a collection automatically.
2. **Set Operations**:
   - Python provides convenient methods like `.intersection()` or operators like `&` for sets.
   - Performing set intersection `set1 & set2` is highly optimized in CPython, running in $O(\min(\text{len}(set1), \text{len}(set2)))$ time on average under the hood.

## Common Mistakes
- **Returning Duplicates**: Forgetting that the problem requires *unique* elements in the intersection. Simply filtering `nums1` elements present in `nums2` without deduplication would fail.
- **Sorting the output unnecessarily**: While some platforms display sorted output, the problem description explicitly states the result can be returned in any order. Sorting it adds an unnecessary $O(K \log K)$ time overhead (where $K$ is the intersection size).
- **Using a list for lookups**: Searching for an item in a list using `item in list` is an $O(N)$ operation. Doing this for every item in another list results in $O(N \times M)$ time complexity, which will TLE (Time Limit Exceeded) for large inputs.

## Alternative Solution
### Two-Pointer Approach (if inputs are sorted or can be sorted)
If the arrays are already sorted, or if we cannot use extra space, we can sort them (takes $O(N \log N + M \log M)$) and use a two-pointer approach to find common elements:
```python
def intersection_two_pointers(nums1: list[int], nums2: list[int]) -> list[int]:
    nums1.sort()
    nums2.sort()
    i, j = 0, 0
    res = set()
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            res.add(nums1[i])
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        else:
            j += 1
    return list(res)
```
- **Time Complexity:** $O(N \log N + M \log M)$ due to sorting.
- **Space Complexity:** $O(1)$ auxiliary space (excluding space needed for the output).

## Interview Tips
- **Always ask if the input is sorted**: If the interviewer says the input is sorted, you should immediately suggest the two-pointer approach to achieve $O(1)$ auxiliary space.
- **Be mindful of constraints**: If the size of one array is significantly smaller than the other (e.g., $N \ll M$), you can optimize the search by sorting the smaller array and binary searching every element of the larger array, or loading the smaller array into a hash map.
