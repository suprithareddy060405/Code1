# Day 009 Notes: Check Whether Two Strings are Anagrams

## Concepts Learned
- **Anagram Normalization**: The step of preprocessing inputs (lowercase, strip whitespace) before comparing.
- **Hash-Map counting cancellation**: Using a single frequency dictionary where we increment counts for one sequence and decrement counts for the other. This saves space and can allow early termination.

## Common Mistakes
- **Sorting to Compare**: Sorting both strings (i.e., `sorted(s1) == sorted(s2)`) is simple to write but costs $O(N \log N)$ time complexity. Hash-map counting is faster ($O(N)$).
- **Not Handling Whitespace or Special Cases**: Often interviewers include spaces or punctuation that should be ignored or handled specifically.
- **Failing early return checks**: Forgetting to check if the lengths of the two cleaned strings match before counting.

## Alternative Solution
Using Python's built-in `collections.Counter`:
```python
from collections import Counter

def is_anagram_counter(s1: str, s2: str) -> bool:
    if s1 is None or s2 is None:
        return s1 == s2
    s1_clean = [c.lower() for c in s1 if not c.isspace()]
    s2_clean = [c.lower() for c in s2 if not c.isspace()]
    return Counter(s1_clean) == Counter(s2_clean)
```
- **Time Complexity**: $O(N + M)$
- **Space Complexity**: $O(K)$

## Interview Tips
- Always check if inputs can contain unicode characters (like accents or emojis) which might complicate sorting or simple ASCII count arrays.
- Emphasize the trade-offs: sorting is $O(N \log N)$ time / $O(1)$ space (in-place), while counting is $O(N)$ time / $O(K)$ space.
