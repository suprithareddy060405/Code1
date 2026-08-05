def count_frequencies(s: str) -> dict:
    """
    Counts the occurrences of each character in a string.
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters.
    """
    # Edge case: Empty string should return an empty dictionary
    if s is None:
        return {}
        
    freq_map = {}
    for char in s:
        # Increment frequency if character is already in dictionary,
        # otherwise initialize count to 1.
        freq_map[char] = freq_map.get(char, 0) + 1
        
    return freq_map


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        ("hello world", {'h': 1, 'e': 1, 'l': 3, 'o': 2, ' ': 1, 'w': 1, 'r': 1, 'd': 1}),
        ("", {}),
        ("AabbCc", {'A': 1, 'a': 1, 'b': 2, 'b': 2, 'C': 1, 'c': 1}), # case-sensitivity check
        ("!!!", {'!': 3}), # special characters
        (None, {}) # None check
    ]

    print("Running Day 007 tests...")
    all_passed = True
    for idx, (string, expected) in enumerate(test_cases, 1):
        result = count_frequencies(string)
        # Note: Order in dict doesn't matter for comparison in Python
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: '{string}' -> Expected: {expected}, Got: {result} [{status}]")
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
