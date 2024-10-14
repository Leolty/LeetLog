# 3212. Count Submatrices With Equal Frequency of X and Y

Difficulty: medium

Link: https://leetcode.com/problems/count-submatrices-with-equal-frequency-of-x-and-y/

Contains PNG: Yes

PNG Links:
- https://assets.leetcode.com/uploads/2024/06/07/examplems.png

## Problem Statement

Given a 2D character matrix `grid`, where `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`, return the number of submatrices that contain:

* `grid[0][0]`
* an **equal** frequency of `'X'` and `'Y'`.
* **at least** one `'X'`.

**Example 1:**

**Input:** grid \= \[\["X","Y","."],\["Y",".","."]]

**Output:** 3

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/06/07/examplems.png)**

**Example 2:**

**Input:** grid \= \[\["X","X"],\["X","Y"]]

**Output:** 0

**Explanation:**

No submatrix has an equal frequency of `'X'` and `'Y'`.

**Example 3:**

**Input:** grid \= \[\[".","."],\[".","."]]

**Output:** 0

**Explanation:**

No submatrix has at least one `'X'`.

**Constraints:**

* `1 <= grid.length, grid[i].length <= 1000`
* `grid[i][j]` is either `'X'`, `'Y'`, or `'.'`.

## Hints

- 1\. Replace `’X’` with 1, `’Y’` with \-1 and `’.’` with 0\.
- 2\. You need to find how many submatrices `grid[0..x][0..y]` have a sum of 0 and at least one `’X’`.
- 3\. Use prefix sum to calculate submatrices sum.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int numberOfSubmatrices(vector<vector<char>>& grid) {
        
    }
};
```

### Java
```java
class Solution {
    public int numberOfSubmatrices(char[][] grid) {
        
    }
}
```

### Python
```python
class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        
```

