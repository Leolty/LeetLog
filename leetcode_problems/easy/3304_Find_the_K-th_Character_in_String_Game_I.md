# 3304. Find the K-th Character in String Game I

Difficulty: easy

Link: https://leetcode.com/problems/find-the-k-th-character-in-string-game-i/

## Problem Statement

Alice and Bob are playing a game. Initially, Alice has a string `word = "a"`.

You are given a **positive** integer `k`.

Now Bob will ask Alice to perform the following operation **forever**:

* Generate a new string by **changing** each character in `word` to its **next** character in the English alphabet, and **append** it to the *original* `word`.

For example, performing the operation on `"c"` generates `"cd"` and performing the operation on `"zb"` generates `"zbac"`.

Return the value of the `kth` character in `word`, after enough operations have been done for `word` to have **at least** `k` characters.

**Note** that the character `'z'` can be changed to `'a'` in the operation.

**Example 1:**

**Input:** k \= 5

**Output:** "b"

**Explanation:**

Initially, `word = "a"`. We need to do the operation three times:

* Generated string is `"b"`, `word` becomes `"ab"`.
* Generated string is `"bc"`, `word` becomes `"abbc"`.
* Generated string is `"bccd"`, `word` becomes `"abbcbccd"`.

**Example 2:**

**Input:** k \= 10

**Output:** "c"

**Constraints:**

* `1 <= k <= 500`

## Hints

- 1\. The constraints are small. Construct the string by simulating the operations.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    char kthCharacter(int k) {
        
    }
};
```

### Java
```java
class Solution {
    public char kthCharacter(int k) {
        
    }
}
```

### Python
```python
class Solution:
    def kthCharacter(self, k: int) -> str:
        
```

