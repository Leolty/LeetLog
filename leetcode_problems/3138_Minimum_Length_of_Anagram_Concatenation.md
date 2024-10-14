# 3138. Minimum Length of Anagram Concatenation

Difficulty: medium

Link: https://leetcode.com/problems/minimum-length-of-anagram-concatenation/

Contains PNG: No

## Problem Statement

You are given a string `s`, which is known to be a concatenation of **anagrams** of some string `t`.

Return the **minimum** possible length of the string `t`.

An **anagram** is formed by rearranging the letters of a string. For example, "aab", "aba", and, "baa" are anagrams of "aab".

**Example 1:**

**Input:** s \= "abba"

**Output:** 2

**Explanation:**

One possible string `t` could be `"ba"`.

**Example 2:**

**Input:** s \= "cdef"

**Output:** 4

**Explanation:**

One possible string `t` could be `"cdef"`, notice that `t` can be equal to `s`.

**Constraints:**

* `1 <= s.length <= 105`
* `s` consist only of lowercase English letters.

## Hints

- 1\. The answer should be a divisor of `s.length`.
- 2\. Check each candidate naively.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minAnagramLength(string s) {
        
    }
};
```

### Java
```java
class Solution {
    public int minAnagramLength(String s) {
        
    }
}
```

### Python
```python
class Solution:
    def minAnagramLength(self, s: str) -> int:
        
```

