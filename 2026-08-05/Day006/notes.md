# Day 006 Notes: Palindrome Checker

## Concepts Learned
- **Two-Pointer Technique**: Useful for traversing data structures (especially arrays and strings) from both ends toward the middle.
- **String Manipulation**: Working with character methods such as `.isalnum()` to filter out special characters, and `.lower()` / `.upper()` for case conversion.
- **In-place traversal**: Achieving space efficiency by pointer-shifting instead of creating new lists or strings.

## Common Mistakes
- **Nested Loops for Non-Alphanumeric Filtering**: It's easy to make index-out-of-bounds mistakes when advancing pointers while looking for alphanumeric characters inside a `while` loop. Always ensure the loop condition `left < right` is checked.
- **High Space Complexity**: Using string slicing like `s[::-1]` after filtering out non-alphanumeric characters. While correct and readable, this takes $O(N)$ extra space.
- **Assuming fixed character sets**: Forgetting that numeric characters (0-9) are alphanumeric and should also be preserved unless specified otherwise.

## Alternative Solution
A very common Pythonic alternative is to filter out the characters and then reverse the string.
```python
def is_palindrome_alt(s: str) -> bool:
    filtered_chars = [char.lower() for char in s if char.isalnum()]
    return filtered_chars == filtered_chars[::-1]
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$ (to store the filtered characters)

## Interview Tips
- Clarify edge cases, such as: "Should we count spaces or symbols?", "Are alphanumeric characters only ASCII, or unicode as well?", and "How should empty strings be handled?".
- If space complexity is critical, always prefer the two-pointer in-place method ($O(1)$ space) over the reversal method ($O(N)$ space).
