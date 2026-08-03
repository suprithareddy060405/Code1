"""
Day 2: Valid Palindrome (Strings)
Language: Python 3
"""


def is_palindrome(s: str) -> bool:
    """
    Checks if a string is a palindrome, ignoring non-alphanumeric characters
    and letter casing.

    Time Complexity: O(N) where N is the length of the string.
    Space Complexity: O(1) auxiliary space.
    """
    left = 0
    right = len(s) - 1

    while left < right:
        # Move left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1

        # Move right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters after converting to lowercase
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Sample Test Cases
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),  # Empty string/only spaces becomes empty, which is a palindrome
        ("ab_a", True),  # Underscore is non-alphanumeric, so "aba" is a palindrome
        ("0P", False),  # Numbers and letters compared
    ]

    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = is_palindrome(test_input)
        assert result == expected, f"Test case {i} failed: Expected {expected}, got {result}"
        print(f"Test case {i} passed: is_palindrome('{test_input}') -> {result}")

    print("All sample test cases executed successfully!")
