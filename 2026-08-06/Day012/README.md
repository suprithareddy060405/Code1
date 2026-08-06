# Find the Second Largest Number in a List

## Problem Statement
Given a list of numbers, find the second largest *distinct* number in the list.

If the list has fewer than 2 unique numbers, return `None`.

## Input Format
- A list of integers `nums`.

## Output Format
- An integer representing the second largest distinct number, or `None` if it does not exist.

## Sample Input 1
```text
[3, 5, 5, 4]
```

## Sample Output 1
```text
4
```

## Sample Input 2
```text
[10, 10, 10]
```

## Sample Output 2
```text
None
```

## Explanation
- In Sample 1, the unique numbers in descending order are `5` and `4`. The second largest is `4`.
- In Sample 2, there is only one unique number (`10`), so there is no second largest distinct number.

## Approach (Single Pass Linear Scan)
We can solve this problem in a single pass with $O(1)$ auxiliary space:
1. Initialize two variables `largest` and `second_largest` to negative infinity (`float('-inf')`).
2. Loop through each number `num` in the list:
   - If `num > largest`, update `second_largest = largest` and `largest = num`.
   - If `num > second_largest` and `num != largest`, update `second_largest = num`.
3. If `second_largest` is still negative infinity, it means no valid second largest element exists. Return `None`. Otherwise, return `second_largest`.

## Complexity Analysis
- **Time Complexity:** $O(N)$ where $N$ is the number of elements in the list. We iterate through the list exactly once.
- **Space Complexity:** $O(1)$ auxiliary space, as we only use two tracking variables.
