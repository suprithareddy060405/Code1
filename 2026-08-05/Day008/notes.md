# Day 008 Notes: Remove Duplicate Characters while Preserving Order

## Concepts Learned
- **Set Data Structure**: Utilized for $O(1)$ average time complexity membership tests (`char not in visited`).
- **Order Preservation**: Standard sets/hash maps do not maintain insertion order in older versions of Python or across languages. Maintaining a separate list or using a ordered dictionary is necessary.
- **String Joins**: Appending characters to a list and calling `"".join(list)` is significantly more efficient in Python than repeatedly concatenating strings using `+` (which creates a new string in memory each time).

## Common Mistakes
- **Naively using `set(s)`**: Converting a string directly to a set (`set(s)`) removes duplicates but destroys the order of the characters.
- **Inefficient membership check**: Using a list to track seen characters and checking `char not in list` leads to an $O(N^2)$ time complexity because lists have $O(N)$ lookup. Always pair tracking lists with a `set` for lookup.

## Alternative Solution
In Python 3.7+, standard dictionaries preserve insertion order. Therefore, we can use `dict.fromkeys()` to remove duplicates while preserving order:
```python
def remove_duplicates_alt(s: str) -> str:
    if not s:
        return ""
    return "".join(dict.fromkeys(s))
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(K)$
This is highly optimized and written in a single line.

## Interview Tips
- Always check if the output needs to be case-sensitive or if casing changes the uniqueness of a character.
- Mention Python's insertion-ordered dictionary behavior, but showcase the list + set approach to demonstrate general DSA principles applicable to any programming language.
