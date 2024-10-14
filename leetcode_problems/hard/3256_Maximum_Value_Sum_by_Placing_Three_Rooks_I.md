# 3256. Maximum Value Sum by Placing Three Rooks I

Difficulty: hard

Link: https://leetcode.com/problems/maximum-value-sum-by-placing-three-rooks-i/

## Problem Statement

You are given a `m x n` 2D array `board` representing a chessboard, where `board[i][j]` represents the **value** of the cell `(i, j)`.

Rooks in the **same** row or column **attack** each other. You need to place *three* rooks on the chessboard such that the rooks **do not** **attack** each other.

Return the **maximum** sum of the cell **values** on which the rooks are placed.

**Example 1:**

**Input:** board \= \[\[\-3,1,1,1],\[\-3,1,\-3,1],\[\-3,2,1,1]]

**Output:** 4

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/08/08/rooks2.png)

We can place the rooks in the cells `(0, 2)`, `(1, 3)`, and `(2, 1)` for a sum of `1 + 1 + 2 = 4`.

**Example 2:**

**Input:** board \= \[\[1,2,3],\[4,5,6],\[7,8,9]]

**Output:** 15

**Explanation:**

We can place the rooks in the cells `(0, 0)`, `(1, 1)`, and `(2, 2)` for a sum of `1 + 5 + 9 = 15`.

**Example 3:**

**Input:** board \= \[\[1,1,1],\[1,1,1],\[1,1,1]]

**Output:** 3

**Explanation:**

We can place the rooks in the cells `(0, 2)`, `(1, 1)`, and `(2, 0)` for a sum of `1 + 1 + 1 = 3`.

**Constraints:**

* `3 <= m == board.length <= 100`
* `3 <= n == board[i].length <= 100`
* `-109 <= board[i][j] <= 109`

## Hints

- 1\. Store the largest 3 values for each row.
- 2\. Select any 3 rows and brute force all combinations.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long maximumValueSum(vector<vector<int>>& board) {
        
    }
};
```

### Java
```java
class Solution {
    public long maximumValueSum(int[][] board) {
        
    }
}
```

### Python
```python
class Solution:
    def maximumValueSum(self, board: List[List[int]]) -> int:
        
```

