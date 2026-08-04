# Notes - Day 3, Problem 5: Sorting & Merging Intervals

## Concepts Learned
1. **Importance of Sorting in Interval Problems**:
   - Many interval-based problems (e.g. merge intervals, insert intervals, meeting rooms) become much simpler once sorted by start times.
   - Sorting establishes a clear relative order, meaning we only ever need to check adjacent elements.
2. **Greedy-like Merging logic**:
   - Keeping track of the running "merged" list and adjusting the right boundary `merged[-1][1]` on the fly is a form of greedy algorithm.
3. **Deep vs. Shallow Copy**:
   - Python's `.sort()` method sorts in-place. If we pass test data directly and sort it, the source list gets modified. Making a deep/shallow copy preserves the original inputs for testing.

## Common Mistakes
- **Neglecting to sort by start coordinate first**: Simply comparing adjacent elements in an unsorted list. For example, in `[[1, 4], [0, 4]]`, without sorting we would fail to merge them since `4 >= 0` isn't adjacent unless sorted.
- **Incorrect overlap condition**: Checking `merged[-1][1] == interval[0]` as non-overlapping. Intervals like `[1, 4]` and `[4, 5]` touch at `4` and must be merged. Thus, the overlap condition is `merged[-1][1] >= interval[0]`.
- **Replacing instead of expanding**: Forgetting to use `max(merged[-1][1], interval[1])` and instead just doing `merged[-1][1] = interval[1]`. If we have `[[1, 10], [2, 3]]`, the second interval is completely inside the first. Simply setting the end to `3` would shrink the interval incorrectly.

## Alternative Solution
### Merging using a Stack
We can use an explicit stack to achieve the same result. The logic is identical but is often explained using stack terminology.
```python
def merge_stack(intervals: list[list[int]]) -> list[list[int]]:
    if not intervals:
        return []
    intervals.sort(key=lambda x: x[0])
    stack = [intervals[0]]
    for i in range(1, len(intervals)):
        top = stack[-1]
        curr = intervals[i]
        if top[1] < curr[0]:
            stack.append(curr)
        elif top[1] < curr[1]:
            top[1] = curr[1]
    return stack
```
- **Time Complexity:** $O(N \log N)$ due to sorting.
- **Space Complexity:** $O(N)$ for the stack.

## Interview Tips
- **Walk through the nested cases**: When drawing examples, always test a case where one interval fully covers another (e.g., `[[1, 5], [2, 3]]`) to demonstrate that you remember to use the `max()` function when merging.
- **Mention space complexity of sorting algorithms**: In Python, Timsort is used, which has $O(N)$ space complexity in the worst case (or $O(1)$ on average for references, but internally it allocates temp runs). Be precise about the language's sorting characteristics.
