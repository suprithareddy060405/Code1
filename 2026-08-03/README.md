# Day 2 - Daily Python Practice

## Problem Name: Valid Palindrome (Check whether a string is a palindrome)

### Problem Statement
A phrase is a **palindrome** if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string `s`, return `True` if it is a palindrome, or `False` otherwise.

### Input Format
- A single string `s`.

### Output Format
- A boolean value (`True` or `False`).

### Constraints
- `1 <= s.length <= 2 * 10^5`
- `s` consists only of printable ASCII characters.

### Sample Input
```python
s = "A man, a plan, a canal: Panama"
```

### Sample Output
```python
True
```

### Explanation
- After removing non-alphanumeric characters and converting to lowercase, the string becomes `"amanaplanacanalpanama"`.
- Since `"amanaplanacanalpanama"` reads the same forward and backward, it is a palindrome.

---

### Approach
We can use the **Two-Pointer Approach** to solve this problem efficiently in $O(N)$ time complexity and $O(1)$ space complexity.
1. Initialize two pointers: `left` at the start of the string (`0`) and `right` at the end of the string (`len(s) - 1`).
2. Move `left` pointer to the right and `right` pointer to the left:
   - If the character at `left` is not alphanumeric, skip it by incrementing `left`.
   - If the character at `right` is not alphanumeric, skip it by decrementing `right`.
   - Once both pointers point to alphanumeric characters, compare them (case-insensitively). If they do not match, return `False`.
   - If they match, increment `left` and decrement `right` to continue checking.
3. If the pointers meet or cross without any mismatch, return `True`.

### Complexity Analysis
- **Time Complexity:** $O(N)$, where $N$ is the length of the string. In the worst case, we traverse each character of the string at most once.
- **Space Complexity:** $O(1)$ auxiliary space, as we are doing the comparisons in-place using pointers without creating any new strings.
