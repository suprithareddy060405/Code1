# Day 010 Notes: Longest Word Finder

## Concepts Learned
- **Character Filtering**: Replacing non-alphanumeric characters with spaces to avoid joining word bounds.
- **Strict Inequality for Tie-Breaking**: Using `>` instead of `>=` preserves the first occurrence when multiple elements share the same maximum size.
- **Tokenization**: Breaking down a long string into distinct semantic tokens (words) using Python's `str.split()`.

## Common Mistakes
- **Splitting by spaces directly**: If you do `sentence.split()`, words like `"coding."` or `"world!!!"` will retain their punctuation, artificially inflating their length.
- **Handling of hyphens/apostrophes**: In some contexts, words like "self-taught" or "user's" might be considered single words. It's important to clarify the definitions of "word" with the interviewer. Here, we defined a word strictly as contiguous alphanumeric characters.

## Alternative Solution
Using Python's built-in `max()` function with a custom key:
```python
import re

def longest_word_regex(sentence: str) -> str:
    # Use regex to find all alphanumeric words
    words = re.findall(r'[a-zA-Z0-9]+', sentence)
    if not words:
        return ""
    # max() returns the first element matching the maximum key in case of ties
    return max(words, key=len)
```
- **Time Complexity**: $O(N)$
- **Space Complexity**: $O(N)$

## Interview Tips
- Always define what a "word" is (e.g. should we include numbers? How to handle punctuation or special characters like hyphens?).
- Clearly explain how ties are handled: "If there are multiple words of the same maximum length, the function returns the first one."
