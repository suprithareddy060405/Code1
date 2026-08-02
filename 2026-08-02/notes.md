# Coding Notes - 2026-08-02

## Concepts Used

1. **Prefix & Suffix Running Products**:
   For any index `i`, the product of all elements except `nums[i]` is the product of all elements to the left of `i` (prefix product) multiplied by the product of all elements to the right of `i` (suffix product).
   
2. **Space Optimization (In-place Calculation)**:
   Instead of allocating separate memory arrays for prefix and suffix products, we reuse the output array (`answer`) to store prefix products. We then iterate backward to multiply with suffix products computed on-the-fly using a single scalar variable `suffix_prod`. This reduces the auxiliary space complexity from $O(n)$ to $O(1)$.

3. **Division-Free Logic**:
   The problem statement explicitly forbids division. The running product approach resolves this elegant constraint. It also naturally handles zeros in the array without raising division-by-zero errors.

---

## Alternative Approaches

### 1. Division-Based Approach (Standard but Forbidden)
* **Concept**: Calculate the product of all elements in the array. Then, for each element, the output is `total_product / nums[i]`.
* **Drawbacks**:
  - Forbidden by the problem statement rules.
  - Requires complex conditional checks to handle zeros:
    - If there is one zero in the array, the product at the zero index is the product of all non-zero elements, while all other indices have a product of zero.
    - If there are two or more zeros, all indices will have a product of zero.
  - Potential division-by-zero exceptions.

### 2. Separate Prefix and Suffix Arrays
* **Concept**:
  - Create a `prefix` array where `prefix[i]` holds the product of all elements from `0` to `i`.
  - Create a `suffix` array where `suffix[i]` holds the product of all elements from `i` to `n-1`.
  - Calculate `answer[i] = prefix[i - 1] * suffix[i + 1]` (with boundary checks).
* **Comparison**:
  - Time Complexity: $O(n)$ (same as optimal).
  - Space Complexity: $O(n)$ auxiliary space because we use two extra arrays of size $n$. This is less optimal than the $O(1)$ auxiliary space approach used in our solution.
