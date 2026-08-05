def remove_duplicates(s: str) -> str:
    """
    Removes duplicate characters from a string while preserving their original order.
    
    Time Complexity: O(n)
    Space Complexity: O(k) where k is the number of unique characters.
    """
    if not s:
        return ""
        
    visited = set()
    result = []
    
    for char in s:
        if char not in visited:
            visited.add(char)
            result.append(char)
            
    return "".join(result)


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        ("google", "gole"),
        ("banana", "ban"),
        ("abcdef", "abcdef"),
        ("a" * 10, "a"),
        ("", ""),
        ("AbAaBb", "AbaB"),  # Case-sensitive check
        ("hello world!", "helo wrd!")  # spaces and punctuation
    ]

    print("Running Day 008 tests...")
    all_passed = True
    for idx, (string, expected) in enumerate(test_cases, 1):
        result = remove_duplicates(string)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: '{string}' -> Expected: '{expected}', Got: '{result}' [{status}]")
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
