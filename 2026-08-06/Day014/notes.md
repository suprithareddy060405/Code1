# Notes - Day 014: Find Duplicate Elements in a List

## Concepts Learned
- **Set Lookup Speed:** Using a `set` for lookup operation `item in seen` is $O(1)$ on average, whereas checking membership in a `list` is $O(N)$. This is why the set approach is $O(N)$ overall, while a nested list approach is $O(N^2)$.
- **Set Properties:** Sets do not allow duplicate values. Adding an item to a set when it already exists is a safe, no-op operation.

## Common Mistakes
- **Nested Loop / List Count Approach:** Doing `if lst.count(item) > 1` inside a loop results in $O(N^2)$ time complexity because `.count()` traverses the entire list of size $N$ for each of the $N$ elements.
- **Returning Duplicated Duplicates:** If an element appears three times (e.g., `[1, 1, 1]`), failing to filter the duplicates collection will result in `[1, 1]` in the output list if not using a set.

## Alternative Solutions
### 1. Using Counter from collections (Count-based)
```python
from collections import Counter

def find_duplicates_counter(lst):
    counts = Counter(lst)
    return [item for item, count in counts.items() if count > 1]
```
- **Time Complexity:** $O(N)$
- **Space Complexity:** $O(N)$
- Note: This is clean and readable, but requires importing the `collections` module.

### 2. Nested Loops (Brute Force - Avoid in Interviews)
Comparing each element with every other element using two loops.
- **Time Complexity:** $O(N^2)$
- **Space Complexity:** $O(1)$ (if editing in-place or returning indices).

## Interview Tips
- Always check if the input list contains mutable/unhashable elements (like nested lists `[[1], [1], [2]]`). Since Python sets require elements to be hashable, you cannot put list objects directly into a set. If that is the case, you'd need alternative comparisons or serialization (e.g., converting lists to tuples).
- Explain the trade-off between time complexity ($O(N)$) and space complexity ($O(N)$) vs. the brute force approach.
- Ask if the output needs to maintain the order of first duplicate occurrence.
