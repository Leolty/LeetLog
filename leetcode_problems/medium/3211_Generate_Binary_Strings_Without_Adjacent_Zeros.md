# 3211. Generate Binary Strings Without Adjacent Zeros

Difficulty: medium

Link: https://leetcode.com/problems/generate-binary-strings-without-adjacent-zeros/

## Problem Statement

You are given a positive integer `n`.

A binary string `x` is **valid** if all substrings of `x` of length 2 contain **at least** one `"1"`.

Return all **valid** strings with length `n`**,** in *any* order.

**Example 1:**

**Input:** n \= 3

**Output:** \["010","011","101","110","111"]

**Explanation:**

The valid strings of length 3 are: `"010"`, `"011"`, `"101"`, `"110"`, and `"111"`.

**Example 2:**

**Input:** n \= 1

**Output:** \["0","1"]

**Explanation:**

The valid strings of length 1 are: `"0"` and `"1"`.

**Constraints:**

* `1 <= n <= 18`

## Hints

- 1\. If we have a string `s` of length `x`, we can generate all strings of length `x + 1`.
- 2\. If `s` has 0 as the last character, we can only append 1, whereas if the last character is 1, we can append both 0 and 1\.
- 3\. We can use recursion and backtracking to generate all such strings.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    vector<string> validStrings(int n) {
        
    }
};
```

### Java
```java
class Solution {
    public List<String> validStrings(int n) {
        
    }
}
```

### Python
```python
class Solution:
    def validStrings(self, n: int) -> List[str]:
        
```

