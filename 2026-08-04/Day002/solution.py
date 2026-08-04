"""
Day 3: Problem 2 - Pow(x, n) (Recursion)
Language: Python 3
"""


def my_pow(x: float, n: int) -> float:
    """
    Calculates x raised to the power n recursively using binary exponentiation.

    Time Complexity: O(log n)
    Space Complexity: O(log n) recursive stack space.
    """
    # Base case
    if n == 0:
        return 1.0

    # Handle negative exponent
    if n < 0:
        x = 1 / x
        n = -n

    # Recursive step
    half = my_pow(x, n // 2)

    # If n is even: x^n = (x^(n/2))^2
    if n % 2 == 0:
        return half * half
    # If n is odd: x^n = x * (x^(n/2))^2
    else:
        return x * half * half


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        # Normal positive even power
        ((2.00000, 10), 1024.00000),
        # Positive odd power
        ((2.10000, 3), 9.26100),
        # Negative power
        ((2.00000, -2), 0.25000),
        # Zero power
        ((5.5, 0), 1.0),
        # Base 0
        ((0.0, 5), 0.0),
        # Negative base with even power
        ((-2.0, 4), 16.0),
        # Negative base with odd power
        ((-2.0, 3), -8.0),
    ]

    for i, ((base, exponent), expected) in enumerate(test_cases, 1):
        result = my_pow(base, exponent)
        # Use a tolerance for floating point comparisons
        assert abs(result - expected) < 1e-9, (
            f"Test case {i} failed: Expected {expected}, got {result}"
        )
        print(f"Test case {i} passed: my_pow({base}, {exponent}) -> {result:.5f}")

    print("All sample test cases executed successfully!")
