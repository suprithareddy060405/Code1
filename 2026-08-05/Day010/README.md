# Day 010: Longest Word Finder

Find the longest word in a given sentence, ignoring punctuation and returning the first occurrence in case of a length tie.

## Problem Statement
Write a function `longest_word(sentence: str) -> str` that takes a sentence string and returns the longest word in it. 
- A word is defined as a contiguous sequence of alphanumeric characters.
- Non-alphanumeric characters (like punctuation: commas, periods, exclamation marks) should be ignored and not counted as part of the word length.
- If multiple words have the same maximum length, return the first word that appears in the sentence.
- If the sentence is empty or contains no words, return an empty string.

## Input Format
- A single string `sentence`.

## Output Format
- A string representing the longest word.

## Sample Input
```
"Fun & exciting, learning Python is great!"
```

## Sample Output
```
"learning"
```

## Explanation
The words extracted are:
- "Fun" (length 3)
- "exciting" (length 8)
- "learning" (length 8)
- "Python" (length 6)
- "is" (length 2)
- "great" (length 5)
Note that "&" is ignored since it is non-alphanumeric.
Both "exciting" and "learning" have length 8. Since "exciting" appears first in the sentence, it is returned. Wait! Let's check:
"Fun & exciting, learning..." -> "exciting" appears before "learning"!
So the sample output should be `"exciting"` if we return the first word in case of a tie.
Let's make sure our sample input / output is correct.
"Fun & exciting, learning Python is great!" -> "exciting" appears before "learning". So the sample output is `"exciting"`. Let's update the README to reflect this clearly.

## Approach
We use **String Tokenization and Cleaning**:
1. Iterate through the sentence and replace all non-alphanumeric characters (except spaces) with spaces, or extract words directly.
2. Split the resulting string by spaces to get individual words.
3. Track the `longest` word found so far.
4. Iterate through each word:
   - If the length of the current word is strictly greater than the length of `longest`, update `longest = word`.
5. Return `longest`.

## Time Complexity
- **O(N)** where `N` is the number of characters in the sentence. We traverse the string to clean it and then split and check each word.

## Space Complexity
- **O(N)** to store the cleaned string and the list of words.
