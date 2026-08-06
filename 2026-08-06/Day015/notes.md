# Notes - Day 015: Linear Search (Without Using Python's 'in' Operator)

## Concepts Learned
- **Linear Search Algorithm:** The simplest searching algorithm that checks every element sequentially until a match is found or the end of the collection is reached.
- **Pythonic Iteration:** Using `enumerate()` is preferred over `range(len(lst))` because it is cleaner and provides both index and value in a single loop step.

## Common Mistakes
- **Using `in` or `.index()`:** Using these violates constraints of basic algorithm implementation exercises, even though they are standard in real-world Python coding.
- **Not Handling Duplicate Targets:** Returning a list of all indices instead of only the *first* occurrence (unless requested). Linear search by default returns the first occurrence index.
- **Off-by-One Errors:** When manually tracking indices, it is easy to make off-by-one errors. Using `enumerate()` avoids this.

## Alternative Solutions
### 1. Simple While Loop (Using Index Tracking)
```python
def linear_search_while(lst, target):
    i = 0
    n = len(lst)
    while i < n:
        if lst[i] == target:
            return i
        i += 1
    return -1
```

### 2. Recursive Linear Search
```python
def linear_search_recursive(lst, target, index=0):
    if index >= len(lst):
        return -1
    if lst[index] == target:
        return index
    return linear_search_recursive(lst, target, index + 1)
```
- Note: Recursion in Python has an overhead and is limited by recursion depth limits, so iteration is preferred.

## Interview Tips
- Linear search is the base algorithm when data is unsorted. If the data is **sorted**, always mention/implement **Binary Search**, which runs in $O(\log N)$ time.
- Emphasize that linear search does not require any additional space ($O(1)$) and works on any iterable (like linked lists), unlike binary search which requires random access (like an array/list).
