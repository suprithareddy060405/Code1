# Day 007: Character Frequency Counter

Count the frequency of each character in a given string.

## Problem Statement
Write a function `count_frequencies(s: str) -> dict` that takes a string `s` and returns a dictionary where keys are the characters present in the string and values are their corresponding frequencies. The counter should be case-sensitive and should count all characters, including spaces and punctuation.

## Input Format
- A single string `s`.

## Output Format
- A dictionary containing character counts.

## Sample Input
```
"hello world"
```

## Sample Output
```
{
    'h': 1,
    'e': 1,
    'l': 3,
    'o': 2,
    ' ': 1,
    'w': 1,
    'r': 1,
    'd': 1
}
```

## Explanation
- 'h', 'e', ' ', 'w', 'r', 'd' appear exactly once.
- 'o' appears twice (in "hell**o**" and "**o**rld").
- 'l' appears three times (in "he**ll**o" and "wor**l**d").

## Approach
We use a **Hash Map / Dictionary**:
1. Initialize an empty dictionary `freq_map`.
2. Iterate through each character `char` in the input string `s`.
3. For each character, check if it already exists in `freq_map`.
   - If it does, increment its value by 1.
   - If it does not, add it to `freq_map` with a value of 1.
4. Return `freq_map`.

## Time Complexity
- **O(N)** where `N` is the length of the string, since we traverse the string once.

## Space Complexity
- **O(K)** where `K` is the number of unique characters in the string (bounded by the character set size, e.g., O(1) for ASCII).
