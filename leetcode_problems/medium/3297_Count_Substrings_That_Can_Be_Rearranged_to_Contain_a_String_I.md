# 3297. Count Substrings That Can Be Rearranged to Contain a String I

Difficulty: medium

Link: https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/

## Problem Statement

You are given two strings `word1` and `word2`.

A string `x` is called **valid** if `x` can be rearranged to have `word2` as a prefix.

Return the total number of **valid** substrings of `word1`.

**Example 1:**

**Input:** word1 \= "bcca", word2 \= "abc"

**Output:** 1

**Explanation:**

The only valid substring is `"bcca"` which can be rearranged to `"abcc"` having `"abc"` as a prefix.

**Example 2:**

**Input:** word1 \= "abcabc", word2 \= "abc"

**Output:** 10

**Explanation:**

All the substrings except substrings of size 1 and size 2 are valid.

**Example 3:**

**Input:** word1 \= "abcabc", word2 \= "aaabc"

**Output:** 0

**Constraints:**

* `1 <= word1.length <= 105`
* `1 <= word2.length <= 104`
* `word1` and `word2` consist only of lowercase English letters.

## Hints

- 1\. Store the frequency of each character for all prefixes.
- 2\. Use Binary Search.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long validSubstringCount(string word1, string word2) {
        
    }
};
```

### Java
```java
class Solution {
    public long validSubstringCount(String word1, String word2) {
        
    }
}
```

### Python
```python
class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        
```

