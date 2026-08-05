# Day 009: Check Whether Two Strings are Anagrams

Check if two strings are anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

## Problem Statement
Write a function `is_anagram(s1: str, s2: str) -> bool` that takes two strings `s1` and `s2` and returns `True` if they are anagrams, and `False` otherwise. The comparison should be case-insensitive and ignore spaces.

## Input Format
- Two strings, `s1` and `s2`.

## Output Format
- A boolean value (`True` or `False`).

## Sample Input
```
s1 = "Listen"
s2 = "Silent"
```

## Sample Output
```
True
```

## Explanation
If we convert both strings to lowercase and ignore any potential spaces, `s1` becomes `"listen"` and `s2` becomes `"silent"`. Both strings contain the exact same set of characters ('l', 'i', 's', 't', 'e', 'n') with the exact same frequencies. Therefore, they are anagrams.

## Approach
We use a **Character Frequency Map**:
1. Check if the normalized lengths of the two strings (after converting to lowercase and removing spaces) are different. If they are, they cannot be anagrams; return `False`.
2. Count the frequencies of each character in `s1` and `s2`.
3. Compare the two frequency maps. If they are identical, return `True`; otherwise, return `False`.

Alternatively, we can use a single dictionary where we increment counts for the first string and decrement counts for the second string. If all counts are zero at the end, the strings are anagrams.

## Time Complexity
- **O(N + M)** where `N` and `M` are the lengths of the two strings, since we traverse both strings to count frequencies.

## Space Complexity
- **O(1)** auxiliary space (or **O(K)** where `K` is the number of unique characters), since the character set size (e.g. 26 lowercase English letters) is constant.
