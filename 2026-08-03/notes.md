# Notes - Day 2: Strings & Palindromes

## Concepts Learned
1. **Two-Pointer Technique**:
   - Useful for searching pairs, reversing, or comparing elements in linear structures (arrays/strings).
   - Helps in achieving $O(1)$ space complexity by avoiding new memory allocations.
2. **String Manipulation Functions**:
   - `str.isalnum()`: Checks if a character is alphanumeric (either a letter or a number).
   - `str.lower()`: Converts a character to lowercase, allowing case-insensitive comparisons.
3. **In-place Processing**:
   - Filtering data directly using pointers rather than building new clean strings first.

## Common Mistakes
- **Neglecting to handle spaces and punctuation**: Forgetting that characters like `,`, `:`, `.`, or spaces are non-alphanumeric and should be skipped.
- **Index Out of Bounds**: Not checking the bounds (`left < right`) while skipping non-alphanumeric characters inside the nested loops.
- **Ignoring Casing**: Comparing uppercase and lowercase characters without normalizing them first.
- **Handling Empty Strings**: Assuming strings will always have alphanumeric characters. An empty string or a string with only non-alphanumeric characters (like `" "`) is considered a valid palindrome.

## Alternative Approach
### 1. Filtering & Reversing (Naive Approach)
Filter out all non-alphanumeric characters, convert them to lowercase, and check if the resulting string is equal to its reverse.
```python
def is_palindrome_naive(s: str) -> bool:
    clean_s = "".join(char.lower() for char in s if char.isalnum())
    return clean_s == clean_s[::-1]
```
- **Time Complexity:** $O(N)$ - We iterate through the string to clean it and then reverse/compare it.
- **Space Complexity:** $O(N)$ - We create a new string containing only the alphanumeric characters.

## Interview Tips
- **Ask Clarifying Questions**:
  - Should the comparison be case-sensitive?
  - Are spaces and special characters ignored?
  - What is the expected behavior for an empty string?
- **Dry Run Your Code**:
  - Always trace your pointers with standard inputs, edge cases (empty strings, single characters), and negative cases (non-palindromes).
- **Highlight Space Complexity**:
  - The naive filtering approach takes $O(N)$ extra space. If memory is a constraint, point out that the two-pointer approach reduces the auxiliary space to $O(1)$.
