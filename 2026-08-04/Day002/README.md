# Problem Name: Pow(x, n)

## Problem Statement
Implement `pow(x, n)`, which calculates $x$ raised to the power $n$ (i.e., $x^n$).

## Sample Input
```python
x = 2.00000
n = 10
```

## Sample Output
```python
1024.00000
```

## Explanation
$2.0^{10} = 1024.0$.

Another example:
`x = 2.10000`, `n = 3`
Output: `9.26100`

`x = 2.00000`, `n = -2`
Output: `0.25000` ($2^{-2} = \frac{1}{4} = 0.25$)

---

## Approach
We use the **Binary Exponentiation (Divide and Conquer)** technique recursively:
1. **Base Case:** Any number raised to the power of 0 is 1. If $n = 0$, return `1.0`.
2. **Negative Powers:** If $n < 0$, we can compute the power for positive $n$ and then return the reciprocal: `pow(x, n) = 1 / pow(x, -n)`.
3. **Recursive Step:**
   - If $n$ is even, $x^n = (x^{n/2})^2$. We can recursively compute `half = pow(x, n // 2)` and return `half * half`.
   - If $n$ is odd, $x^n = x \times (x^{(n-1)/2})^2$. We can return `x * pow(x, n - 1)` or `x * half * half` where `half = pow(x, n // 2)`.

This reduces the number of multiplications from $O(n)$ to $O(\log n)$.

## Time Complexity
- **Time Complexity:** $O(\log n)$ since the exponent $n$ is halved in each recursive step.

## Space Complexity
- **Space Complexity:** $O(\log n)$ auxiliary space due to the recursive call stack.
