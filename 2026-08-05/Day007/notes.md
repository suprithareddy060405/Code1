# Day 007 Notes: Character Frequency Counter

## Concepts Learned
- **Hash Maps / Dictionaries**: Using keys to represent elements and values to represent their frequency count.
- **Retrieval with Defaults**: The utility of `dict.get(key, default)` to avoid `KeyError` checks and write cleaner pythonic code.
- **Collections module**: Python has built-in optimizations like `collections.Counter` and `collections.defaultdict` which simplify frequency counting.

## Common Mistakes
- **KeyError Exceptions**: Accessing `freq_map[char]` directly without checking if `char in freq_map` first.
- **Inefficient Searching**: Using `s.count(char)` for each character, which leads to an $O(N^2)$ time complexity. Always build a single frequency map in $O(N)$ time.
- **Ignoring Whitespace/Case requirements**: Failing to confirm if the frequency map needs to group uppercase/lowercase together, or if spaces/punctuation should be skipped.

## Alternative Solution
Using Python's built-in `collections.Counter`:
```python
from collections import Counter

def count_frequencies_counter(s: str) -> dict:
    if s is None:
        return {}
    return dict(Counter(s))
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(K)$

## Interview Tips
- Clarify whether the count is case-sensitive and whether spaces/punctuation should be included in the count.
- Mention `collections.Counter` to the interviewer to show Python standard library proficiency, but be ready to write the raw dictionary/hash map implementation from scratch.
