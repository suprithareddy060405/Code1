# Count Words in a Sentence

## Problem Statement
Write a Python function that takes a sentence (string) as input and returns the total number of words in it. 

A word is defined as a sequence of non-space characters separated by one or more spaces. The solution must properly handle edge cases such as leading/trailing spaces and multiple consecutive spaces between words.

## Input Format
- A single string `sentence`.

## Output Format
- An integer representing the count of words in the sentence.

## Sample Input
```text
"  Hello   World, welcome to Python!   "
```

## Sample Output
```text
5
```

## Explanation
The sentence has leading and trailing spaces and multiple spaces between "Hello" and "World,". Discarding these extra spaces, we have 5 distinct words: `"Hello"`, `"World,"`, `"welcome"`, `"to"`, and `"Python!"`.

## Approach
1. Use Python's built-in string method `.split()`. 
2. When `.split()` is called without arguments, it automatically groups consecutive whitespaces together and treats them as a single separator. It also discards any leading or trailing whitespaces from the resulting list.
3. Return the length of the list of words.

## Complexity Analysis
- **Time Complexity:** $O(N)$, where $N$ is the length of the sentence. We must traverse the string to split it.
- **Space Complexity:** $O(N)$, to store the split words in a list of size proportional to the input string.
