# Linear Search (Without Using Python's 'in' Operator)

## Problem Statement
Implement the linear search algorithm in Python. Given a list of elements and a target element, find the index of the first occurrence of the target in the list.

**Constraint:** You are NOT allowed to use Python's built-in `in` operator for membership testing or the list `.index()` method. You must implement the search manually. If the target is not found in the list, return `-1`.

## Input Format
- A list of elements `lst`.
- The `target` element to find.

## Output Format
- An integer representing the 0-based index of the target, or `-1` if the target is not present in the list.

## Sample Input 1
```text
lst = [4, 2, 7, 1, 9]
target = 7
```

## Sample Output 1
```text
2
```

## Sample Input 2
```text
lst = [4, 2, 7, 1, 9]
target = 5
```

## Sample Output 2
```text
-1
```

## Explanation
- In Sample 1, the target `7` is found at index `2`.
- In Sample 2, the target `5` does not exist in the list, so we return `-1`.

## Approach
1. Iterate through the list element-by-element using `enumerate()` to keep track of both the index and the element value.
2. In each iteration, compare the current element with the target.
3. If a match is found, return the current index immediately.
4. If the loop completes without finding a match, return `-1`.

## Complexity Analysis
- **Time Complexity:** 
  - **Best Case:** $O(1)$ if the target is the first element of the list.
  - **Average/Worst Case:** $O(N)$ where $N$ is the length of the list, since we may have to scan all elements.
- **Space Complexity:** $O(1)$ auxiliary space, since we only use a loop and index tracker.
