def is_palindrome(s: str) -> bool:
    """
    Checks if a given string is a palindrome, ignoring non-alphanumeric characters
    and character casing.
    
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    # Edge case: Empty string or single character is always a palindrome
    if not s or len(s) == 1:
        return True

    left, right = 0, len(s) - 1

    while left < right:
        # Move left pointer past non-alphanumeric characters
        while left < right and not s[left].isalnum():
            left += 1
        
        # Move right pointer past non-alphanumeric characters
        while left < right and not s[right].isalnum():
            right -= 1

        # Compare characters in a case-insensitive manner
        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("No 'x' in Nixon", True),
        ("12321", True),
        ("123421", False),
        ("a", True),
        (".,", True)  # only non-alphanumeric characters
    ]

    print("Running Day 006 tests...")
    all_passed = True
    for idx, (string, expected) in enumerate(test_cases, 1):
        result = is_palindrome(string)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: '{string}' -> Expected: {expected}, Got: {result} [{status}]")
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
