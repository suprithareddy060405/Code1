# Daily Python Practice - 2026-08-02

## Problem Statement: Product of Array Except Self

Given an integer array `nums`, return an array `answer` such that `answer[i]` is equal to the product of all the elements of `nums` except `nums[i]`.

The product of any prefix or suffix of `nums` is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in $O(n)$ time and without using the division operation.

### Examples

**Example 1:**
- **Input:** `nums = [1, 2, 3, 4]`
- **Output:** `[24, 12, 8, 6]`

**Example 2:**
- **Input:** `nums = [-1, 1, 0, -3, 3]`
- **Output:** `[0, 0, 9, 0, 0]`

---

## Approach

To solve this problem in $O(n)$ time complexity and $O(1)$ auxiliary space (excluding the output array), we use a prefix and suffix product accumulation strategy.

1. **Initialize the Answer Array**: Create an array `answer` of the same length as `nums`, and initialize `answer[0] = 1`.
2. **First Pass (Prefix Products)**: Iterate through the array from left to right. For each index `i`, calculate the product of all elements to the left of `i` and store it in `answer[i]`. Specifically:
   $$answer[i] = answer[i - 1] \times nums[i - 1]$$
3. **Second Pass (Suffix Products)**: Iterate through the array from right to left. Use a single running product variable `suffix_prod` (initialized to `1`) to keep track of the product of all elements to the right of `i`. Multiply `answer[i]` by `suffix_prod` (i.e., `answer[i] *= suffix_prod`), and then update `suffix_prod` by multiplying it with `nums[i]` (i.e., `suffix_prod *= nums[i]`).
4. Return `answer`.

---

## Complexity Analysis

- **Time Complexity:** $O(n)$ since we iterate through the input array of size $n$ exactly twice (once forward, once backward).
- **Space Complexity:** $O(1)$ auxiliary space. The output array `answer` does not count as extra space for the purpose of space complexity analysis, and we only use a single `suffix_prod` integer variable for running calculations.
