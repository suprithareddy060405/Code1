def longest_word(sentence: str) -> str:
    """
    Finds the longest word in a sentence, ignoring punctuation.
    Returns the first occurrence in case of a tie.
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not sentence:
        return ""
        
    # Replace any non-alphanumeric character with a space
    # This separates words cleanly even if they are attached to punctuation
    cleaned_chars = []
    for char in sentence:
        if char.isalnum():
            cleaned_chars.append(char)
        else:
            cleaned_chars.append(" ")
            
    cleaned_sentence = "".join(cleaned_chars)
    words = cleaned_sentence.split()
    
    if not words:
        return ""
        
    longest = ""
    for word in words:
        # Strict inequality ensures we keep the first occurrence in case of ties
        if len(word) > len(longest):
            longest = word
            
    return longest


if __name__ == "__main__":
    # Test Cases
    test_cases = [
        ("Fun & exciting, learning Python is great!", "exciting"),
        ("I love coding in Python.", "coding"),
        ("Hello, world!!!", "Hello"),  # Tie case, "Hello" vs "world" (both len 5), returns first
        ("     ", ""),  # Only spaces
        ("", ""),  # Empty string
        ("A-B-C-D-E", "A"),  # non-alnum hyphen separator
        ("Python3 is awesome!", "Python3")  # includes numbers
    ]

    print("Running Day 010 tests...")
    all_passed = True
    for idx, (sentence, expected) in enumerate(test_cases, 1):
        result = longest_word(sentence)
        status = "PASSED" if result == expected else "FAILED"
        print(f"Test {idx}: '{sentence}' -> Expected: '{expected}', Got: '{result}' [{status}]")
        if result != expected:
            all_passed = False
            
    if all_passed:
        print("All tests passed successfully!")
    else:
        print("Some tests failed.")
