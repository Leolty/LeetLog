# 3240. Minimum Number of Flips to Make Binary Grid Palindromic II

Difficulty: medium

Link: https://leetcode.com/problems/minimum-number-of-flips-to-make-binary-grid-palindromic-ii/

Contains PNG: Yes

PNG Links:
- https://assets.leetcode.com/uploads/2024/08/01/image.png
- https://assets.leetcode.com/uploads/2024/07/08/screenshot-from-2024-07-09-01-37-48.png
- https://assets.leetcode.com/uploads/2024/08/01/screenshot-from-2024-08-01-23-05-26.png

## Problem Statement

You are given an `m x n` binary matrix `grid`.

A row or column is considered **palindromic** if its values read the same forward and backward.

You can **flip** any number of cells in `grid` from `0` to `1`, or from `1` to `0`.

Return the **minimum** number of cells that need to be flipped to make **all** rows and columns **palindromic**, and the total number of `1`'s in `grid` **divisible** by `4`.

**Example 1:**

**Input:** grid \= \[\[1,0,0],\[0,1,0],\[0,0,1]]

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/08/01/image.png)

**Example 2:**

**Input:** grid \= \[\[0,1],\[0,1],\[0,0]]

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/08/screenshot-from-2024-07-09-01-37-48.png)

**Example 3:**

**Input:** grid \= \[\[1],\[1]]

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/08/01/screenshot-from-2024-08-01-23-05-26.png)

**Constraints:**

* `m == grid.length`
* `n == grid[i].length`
* `1 <= m * n <= 2 * 105`
* `0 <= grid[i][j] <= 1`

## Hints

- 1\. For each `(x, y)`, find `(m - 1 - x, y)`, `(m - 1 - x, n - 1 - y)`, and `(x, n - 1 - y)`; they should be the same.
- 2\. Note that we need to specially handle the middle row (column) if the number of rows (columns) is odd.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minFlips(vector<vector<int>>& grid) {
        
    }
};
```

### Java
```java
class Solution {
    public int minFlips(int[][] grid) {
        
    }
}
```

### Python
```python
class Solution:
    def minFlips(self, grid: List[List[int]]) -> int:
        
```

