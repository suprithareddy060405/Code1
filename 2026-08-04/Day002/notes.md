# Notes - Day 3, Problem 2: Recursion & Binary Exponentiation

## Concepts Learned
1. **Divide and Conquer (Binary Exponentiation)**:
   - Instead of multiplying $x$ by itself $n$ times ($O(n)$ steps), we divide the exponent $n$ by $2$ at each step ($O(\log n)$ steps).
   - This showcases how mathematical properties can reduce computational complexity significantly.
2. **Handling Negative Exponents recursively**:
   - $x^{-n} = (\frac{1}{x})^n$. By taking the reciprocal of $x$ and turning $n$ positive, we reuse the positive exponent logic.
3. **Float Precision**:
   - Floating-point calculations can introduce tiny rounding errors (e.g. $9.261000000000001$ instead of $9.261$).
   - When asserting float correctness in Python, it's best to check if `abs(a - b) < epsilon` rather than strict equality `a == b`.

## Common Mistakes
- **Stack Overflow (Recursion Limit)**: Running simple recursion without halving the search space (like $x^n = x \times x^{n-1}$) on a large $n$ (e.g., $n = 10^9$) will raise a `RecursionError`.
- **Integer Division vs Float Division**: Using `/` instead of `//` for dividing the exponent. In Python, `n / 2` returns a float, which causes type mismatches or infinite loops if not converted back to an integer.
- **Handling $n = -2^{31}$ (Integer Overflow)**: In other languages like Java or C++, negating $n$ when $n = -2^{31}$ causes integer overflow. In Python, integers have arbitrary precision, but it's still a good edge case to be aware of.

## Alternative Solution
### Iterative Binary Exponentiation
An iterative version of binary exponentiation avoids recursive stack space, reducing the space complexity to $O(1)$.
```python
def my_pow_iterative(x: float, n: int) -> float:
    if n == 0:
        return 1.0
    if n < 0:
        x = 1 / x
        n = -n

    result = 1.0
    current_product = x
    while n > 0:
        if n % 2 == 1:
            result *= current_product
        current_product *= current_product
        n //= 2
    return result
```
- **Time Complexity:** $O(\log n)$
- **Space Complexity:** $O(1)$ auxiliary space.

## Interview Tips
- **Mention Space Optimization**: If you solve it recursively, immediately point out that the iterative version achieves $O(1)$ space complexity by avoiding the call stack.
- **Floating Point Constraints**: Mention that division by zero (e.g., `x = 0`, `n < 0`) is mathematically undefined and ask how it should be handled (raising an Exception vs returning infinity).
