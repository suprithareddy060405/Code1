# Merge Two Dictionaries

## Problem Statement
Write a Python function that takes two dictionaries as input and merges them into a single dictionary. 

If there are overlapping keys present in both dictionaries, the value from the second dictionary should overwrite the value from the first dictionary. The function should return a *new* dictionary and not mutate the input dictionaries.

## Input Format
- Two dictionaries, `dict1` and `dict2`.

## Output Format
- A new dictionary containing key-value pairs from both input dictionaries.

## Sample Input
```python
dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 99, 'c': 4}
```

## Sample Output
```python
{'a': 1, 'b': 99, 'c': 4}
```

## Explanation
The keys `'a'` and `'c'` are unique to `dict1` and `dict2` respectively, so their values are preserved. The key `'b'` is present in both dictionaries; therefore, its value from the second dictionary (`99`) overwrites the value from the first dictionary (`2`).

## Approach
In modern Python (Python 3.9+), we can use the merge operator (`|`) to merge two dictionaries:
`merged_dict = dict1 | dict2`

For older Python versions (Python 3.5 to 3.8), dictionary unpacking (`{**dict1, **dict2}`) or `.copy()` followed by `.update()` is used.

We will use the modern merge operator `|` as the primary solution, and document other methods in the notes.

## Complexity Analysis
- **Time Complexity:** $O(N + M)$ where $N$ is the number of elements in `dict1` and $M$ is the number of elements in `dict2`. We have to copy the elements of both dictionaries into a new one.
- **Space Complexity:** $O(N + M)$ to store the merged dictionary containing elements from both inputs.
