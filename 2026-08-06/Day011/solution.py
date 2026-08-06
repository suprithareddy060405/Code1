def count_words(sentence: str) -> int:
    """
    Counts the number of words in a given sentence.

    A word is defined as a sequence of non-space characters.
    Handles multiple spaces, leading, and trailing whitespaces.

    Args:
        sentence (str): The input sentence.

    Returns:
        int: The number of words in the sentence.
    """
    # Guard clause: if the input is None or an empty string, return 0
    if not sentence:
        return 0

    # split() with no arguments splits the string at any whitespace
    # and automatically discards consecutive spaces and leading/trailing spaces.
    words = sentence.split()
    return len(words)


if __name__ == "__main__":
    # Sample Test Cases
    test_cases = [
        ("  Hello   World, welcome to Python!   ", 5),
        ("", 0),
        ("   ", 0),
        ("SingleWord", 1),
        ("Python is fun.", 3)
    ]

    for i, (text, expected) in enumerate(test_cases):
        result = count_words(text)
        assert result == expected, f"Test {i+1} failed: expected {expected}, got {result}"
        print(f"Test {i+1} passed: '{text}' -> {result}")
