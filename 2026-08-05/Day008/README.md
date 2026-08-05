# Day 008: Remove Duplicate Characters while Preserving Order

Remove all duplicate characters from a string, keeping only the first occurrence of each character, and preserving the original order of characters.

## Problem Statement
Write a function `remove_duplicates(s: str) -> str` that takes a string `s` and returns a new string where all duplicate characters have been removed. The order of the remaining unique characters should match their original order of appearance in `s`.

## Input Format
- A single string `s`.

## Output Format
- A string with duplicates removed.

## Sample Input
```
"google"
```

## Sample Output
```
"gole"
```

## Explanation
- 'g' appears at index 0 and index 3. Only the first occurrence (index 0) is kept.
- 'o' appears at index 1 and index 2. Only the first occurrence (index 1) is kept.
- 'l' and 'e' appear once and are preserved in their relative order.
- The output is "gole".

## Approach
We use a **Tracking Set**:
1. Initialize an empty list `result` and an empty set `visited`.
2. Iterate through each character `char` in the input string `s`.
3. If `char` is not in the `visited` set:
   - Add it to `visited`.
   - Append it to `result`.
4. Join the elements of `result` into a single string and return it.

Using a set for membership check ensures $O(1)$ lookups, maintaining an overall linear time complexity.

## Time Complexity
- **O(N)** where `N` is the length of the string, since we traverse the string once and lookup/add in a set in $O(1)$ time.

## Space Complexity
- **O(K)** where `K` is the number of unique characters in the string (used by the set and list). In the worst case, $O(N)$ when all characters are unique.
