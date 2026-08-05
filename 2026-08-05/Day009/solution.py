def is_anagram(s1: str, s2: str) -> bool:
    """
    Checks if two strings are anagrams of each other,
    ignoring case and whitespace characters.
    
    Time Complexity: O(n + m)
    Space Complexity: O(1) assuming a fixed-size character set.
    """
    # Handle None inputs
    if s1 is None or s2 is None:
        return s1 == s2
        
    # Clean the strings: convert to lowercase and remove spaces
    s1_clean = "".join(char.lower() for char in s1 if not char.isspace())
    s2_clean = "".join(char.lower() for char in s2 if not char.isspace())
    
    # If lengths differ, they cannot be anagrams
    if len(s1_clean) != len(s2_clean):
        return False
        
    # Count frequencies
    char_counts = {}
    for char in s1_clean:
        char_counts[char] = char_counts.get(char, 0) + 1
        
    # Decrement counts using the second string
    for char in s2_clean:
        if char not in char_counts:
            return False
        char_counts[char] -= 1
        if char_counts[char] < 0:
            return False
            
    # Check if all counts are zero (implicitly True if we didn't exit early, 
    # since lengths are equal and we never went below 0).
    return True


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        (("Listen", "Silent"), True),
        (("anagram", "nagaram"), True),
        (("rat", "car"), False),
        (("", ""), True),
        (("A gentleman", "Elegant man"), True), # contains spaces and different casing
        (("a", "ab"), False),
        (("ab", "a"), False),
        ((None, None), True)
    ]

    print("Running Day 009 tests...")
    all_passed = True
    for idx, ((str1, str2), expected) in enumerate(test_cases, 1):
        result = is_anagram(str1, str2)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: ('{str1}', '{str2}') -> Expected: {expected}, Got: {result} [{status}]")
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
