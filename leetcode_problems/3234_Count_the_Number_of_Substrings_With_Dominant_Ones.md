# 3234. Count the Number of Substrings With Dominant Ones

Difficulty: medium

Link: https://leetcode.com/problems/count-the-number-of-substrings-with-dominant-ones/

Contains PNG: No

## Problem Statement

You are given a binary string `s`.

Return the number of substrings with **dominant** ones.

A string has **dominant** ones if the number of ones in the string is **greater than or equal to** the **square** of the number of zeros in the string.

**Example 1:**

**Input:** s \= "00011"

**Output:** 5

**Explanation:**

The substrings with dominant ones are shown in the table below.

| i | j | s\[i..j] | Number of Zeros | Number of Ones |
| --- | --- | --- | --- | --- |
| 3 | 3 | 1 | 0 | 1 |
| 4 | 4 | 1 | 0 | 1 |
| 2 | 3 | 01 | 1 | 1 |
| 3 | 4 | 11 | 0 | 2 |
| 2 | 4 | 011 | 1 | 2 |

**Example 2:**

**Input:** s \= "101101"

**Output:** 16

**Explanation:**

The substrings with **non\-dominant** ones are shown in the table below.

Since there are 21 substrings total and 5 of them have non\-dominant ones, it follows that there are 16 substrings with dominant ones.

| i | j | s\[i..j] | Number of Zeros | Number of Ones |
| --- | --- | --- | --- | --- |
| 1 | 1 | 0 | 1 | 0 |
| 4 | 4 | 0 | 1 | 0 |
| 1 | 4 | 0110 | 2 | 2 |
| 0 | 4 | 10110 | 2 | 3 |
| 1 | 5 | 01101 | 2 | 3 |

**Constraints:**

* `1 <= s.length <= 4 * 104`
* `s` consists only of characters `'0'` and `'1'`.

## Hints

- 1\. Let us fix the starting index `l` of the substring and count the number of indices `r` such that `l <= r` and the substring `s[l..r]` has dominant ones.
- 2\. A substring with dominant ones has at most `sqrt(n)` zeros.
- 3\. We cannot iterate over every `r` and check if the `s[l..r]` has dominant ones. Instead, we iterate over the next `sqrt(n)` zeros to the left of `l` and count the number of substrings with dominant ones where the current zero is the rightmost zero of the substring.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int numberOfSubstrings(string s) {
        
    }
};
```

### Java
```java
class Solution {
    public int numberOfSubstrings(String s) {
        
    }
}
```

### Python
```python
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        
```

