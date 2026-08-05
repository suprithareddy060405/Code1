# Day 006: Palindrome Checker

Check if a given string is a palindrome. A string is considered a palindrome if it reads the same forward and backward, ignoring case and non-alphanumeric characters.

## Problem Statement
Write a function `is_palindrome(s: str) -> bool` that takes a string `s` and returns `True` if it is a palindrome, and `False` otherwise. You should ignore character casing (e.g., 'A' and 'a' are treated as the same) and disregard all non-alphanumeric characters (spaces, punctuation, symbols).

## Input Format
- A single string `s`.

## Output Format
- Returns a boolean value (`True` or `False`).

## Sample Input
```
"A man, a plan, a canal: Panama"
```

## Sample Output
```
True
```

## Explanation
If we remove all non-alphanumeric characters and convert the string to lowercase, we get `"amanaplanacanalpanama"`. Reading this string forward and backward yields the exact same characters, so it is a palindrome.

## Approach
We use the **Two-Pointer Technique**:
1. Initialize two pointers: `left` at the start of the string (index `0`) and `right` at the end of the string (index `len(s) - 1`).
2. Move the `left` pointer to the right if it points to a non-alphanumeric character.
3. Move the `right` pointer to the left if it points to a non-alphanumeric character.
4. If both pointers point to alphanumeric characters, compare them (case-insensitive).
   - If they do not match, return `False`.
   - If they match, increment `left` and decrement `right`.
5. Repeat until `left` >= `right`. If no mismatch is found, return `True`.

## Time Complexity
- **O(N)** where `N` is the length of the string, since we traverse the string at most once.

## Space Complexity
- **O(1)** auxiliary space because we do the comparison in-place using two pointers, without creating a new filtered string.
