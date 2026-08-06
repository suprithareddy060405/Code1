# Notes - Day 013: Merge Two Dictionaries

## Concepts Learned
- **Dictionary Operators:** Python 3.9 introduced the merge operator (`|`) and update operator (`|=`) for dictionaries.
- **Immutability vs Mutation:** Standard dictionary methods like `update()` mutate the dictionary in-place, whereas operators like `|` or unpacking `{**d1, **d2}` create a new dictionary, preserving the original inputs.

## Common Mistakes
- **Mutating Inputs Unexpectedly:** Using `dict1.update(dict2)` directly on the input argument without copying it first will mutate `dict1`. If the caller of your function doesn't expect `dict1` to be changed, this can introduce side-effects and bugs.
- **Incorrect Order of Arguments:** If you want `dict2` to overwrite `dict1`, the order must be `dict1 | dict2` or `{**dict1, **dict2}`. Reversing the order (`dict2 | dict1`) would cause values from `dict1` to overwrite `dict2`.

## Alternative Solutions
### 1. Dictionary Unpacking (Python 3.5+)
```python
def merge_dictionaries_unpack(dict1, dict2):
    return {**dict1, **dict2}
```

### 2. Copy and Update (Compatible with all Python versions)
```python
def merge_dictionaries_copy_update(dict1, dict2):
    merged = dict1.copy()
    merged.update(dict2)
    return merged
```

## Interview Tips
- Always check if the interviewer expects you to mutate one of the input dictionaries in-place or return a new one. A clean, non-mutating approach is generally safer.
- Show depth of language knowledge by explaining the different methods to merge dictionaries across various Python versions.
- Discuss what happens when nested dictionaries are merged (deep merge vs shallow merge). The methods discussed here all perform a **shallow merge**.
