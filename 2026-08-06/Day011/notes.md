# Notes - Day 011: Count Words in a Sentence

## Concepts Learned
- **String Splitting:** Python's `str.split()` method behaves differently when called without arguments vs. when called with a specific separator like `split(' ')`.
  - `split()` with no arguments splits by any run of consecutive whitespace characters (spaces, tabs, newlines) and strips leading/trailing whitespace.
  - `split(' ')` splits on every single space character, which can lead to empty strings `""` in the resulting list if there are multiple consecutive spaces.
- **Handling Edge Cases:** Checking for empty input strings and strings consisting only of whitespaces.

## Common Mistakes
- **Using `sentence.split(" ")`:** This returns elements like `""` (empty strings) when there are multiple consecutive spaces. For example, `"a  b".split(" ")` returns `['a', '', 'b']` (length 3 instead of 2).
- **Not Handling None or Empty Inputs:** Forgetting to check if the string is empty or contains only spaces, which could cause bugs if indexing or processing.

## Alternative Solution
A manual character-by-character iteration that tracks space transitions:
```python
def count_words_manual(sentence: str) -> int:
    count = 0
    in_word = False
    for char in sentence:
        if char != ' ':
            if not in_word:
                count += 1
                in_word = True
        else:
            in_word = False
    return count
```
This approach avoids list allocation, giving $O(1)$ auxiliary space complexity.

## Interview Tips
- Clarify with the interviewer: "Are punctuation marks treated as part of the word?" (e.g., in "Hello, World", does "Hello," count as one word?). Usually, yes, unless specified otherwise.
- Ask if non-space whitespaces (tabs `\t`, newlines `\n`) should also count as delimiters.
