# Find Duplicate Elements in a List

## Problem Statement
Given a list of elements, write a Python function to find all the elements that appear more than once (duplicates). The resulting list of duplicates should only contain unique values (i.e., no duplicates in the duplicates list itself).

## Input Format
- A list of elements `lst`.

## Output Format
- A list of duplicate elements.

## Sample Input
```text
[1, 2, 3, 2, 4, 5, 1, 2]
```

## Sample Output
```text
[1, 2]
```

## Explanation
- The number `1` appears 2 times.
- The number `2` appears 3 times.
- The number `3`, `4`, and `5` appear only once.
- The duplicates are `1` and `2`. Even though `2` appears multiple times, it is listed only once in the output.

## Approach
1. Initialize two sets: `seen` (to track elements encountered so far) and `duplicates` (to track elements seen more than once).
2. Iterate through each element in the input list:
   - If the element is already in `seen`, add it to the `duplicates` set.
   - If not, add it to `seen`.
3. Convert the `duplicates` set to a list and return it.

## Complexity Analysis
- **Time Complexity:** $O(N)$ where $N$ is the number of elements in the list, as set lookups and insertions are $O(1)$ on average.
- **Space Complexity:** $O(N)$ auxiliary space, to store elements in `seen` and `duplicates` sets.
