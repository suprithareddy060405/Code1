# Problem Name: Merge Intervals

## Problem Statement
Given an array of `intervals` where `intervals[i] = [start_i, end_i]`, merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

## Sample Input
```python
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
```

## Sample Output
```python
[[1, 6], [8, 10], [15, 18]]
```

## Explanation
Since intervals `[1, 3]` and `[2, 6]` overlap, they are merged into `[1, 6]`.
The rest of the intervals `[8, 10]` and `[15, 18]` do not overlap, so they remain unchanged.

Another example:
`intervals = [[1, 4], [4, 5]]`
Output: `[[1, 5]]` (intervals overlap at boundary value `4`).

---

## Approach
We can solve this problem efficiently using **Sorting**:
1. **Sort** the intervals based on their start coordinates: `intervals.sort(key=lambda x: x[0])`. Sorting makes sure that any potentially overlapping intervals are adjacent to each other.
2. Initialize an empty list `merged = []` to store the final list of merged intervals.
3. Iterate through each interval in the sorted list:
   - If `merged` is empty, or if the current interval's start coordinate is greater than the end coordinate of the last interval in `merged` (i.e. `merged[-1][1] < interval[0]`), it means there is no overlap. We simply append the current interval to `merged`.
   - If there is an overlap, we merge them by updating the end coordinate of the last interval in `merged` to be the maximum of its own end coordinate and the current interval's end coordinate (i.e. `merged[-1][1] = max(merged[-1][1], interval[1])`).
4. Return `merged`.

## Time Complexity
- **Time Complexity:** $O(N \log N)$ where $N$ is the number of intervals. Sorting the array takes $O(N \log N)$ time, and the subsequent linear scan takes $O(N)$ time.

## Space Complexity
- **Space Complexity:** $O(N)$ (or $O(\log N)$ depending on language-specific sort implementation details) for storing the sorted intervals and output.
