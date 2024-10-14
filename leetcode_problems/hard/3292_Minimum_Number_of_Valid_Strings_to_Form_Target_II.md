# 3292. Minimum Number of Valid Strings to Form Target II

Difficulty: hard

Link: https://leetcode.com/problems/minimum-number-of-valid-strings-to-form-target-ii/

## Problem Statement

You are given an array of strings `words` and a string `target`.

A string `x` is called **valid** if `x` is a prefix of **any** string in `words`.

Return the **minimum** number of **valid** strings that can be *concatenated* to form `target`. If it is **not** possible to form `target`, return `-1`.

**Example 1:**

**Input:** words \= \["abc","aaaaa","bcdef"], target \= "aabcdabc"

**Output:** 3

**Explanation:**

The target string can be formed by concatenating:

* Prefix of length 2 of `words[1]`, i.e. `"aa"`.
* Prefix of length 3 of `words[2]`, i.e. `"bcd"`.
* Prefix of length 3 of `words[0]`, i.e. `"abc"`.

**Example 2:**

**Input:** words \= \["abababab","ab"], target \= "ababaababa"

**Output:** 2

**Explanation:**

The target string can be formed by concatenating:

* Prefix of length 5 of `words[0]`, i.e. `"ababa"`.
* Prefix of length 5 of `words[0]`, i.e. `"ababa"`.

**Example 3:**

**Input:** words \= \["abcdef"], target \= "xyz"

**Output:** \-1

**Constraints:**

* `1 <= words.length <= 100`
* `1 <= words[i].length <= 5 * 104`
* The input is generated such that `sum(words[i].length) <= 105`.
* `words[i]` consists only of lowercase English letters.
* `1 <= target.length <= 5 * 104`
* `target` consists only of lowercase English letters.

## Hints

- 1\. Let `dp[i]` be the minimum cost to form the prefix of length `i` of `target`.
- 2\. Use Rabin\-Karp to hash every prefix and store it in a HashSet.
- 3\. Use Binary search to find the longest substring starting at index `i` (`target[i..j]`) that has a hash present in the HashSet.
- 4\. Inverse Modulo precomputation can optimise hash calculation.
- 5\. Use Lazy Segment Tree, or basic Segment Tree to update `dp[i..j]`.
- 6\. Is it possible to use two TreeSets to update `dp[i..j]`?

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minValidStrings(vector<string>& words, string target) {
        
    }
};
```

### Java
```java
class Solution {
    public int minValidStrings(String[] words, String target) {
        
    }
}
```

### Python
```python
class Solution:
    def minValidStrings(self, words: List[str], target: str) -> int:
        
```

