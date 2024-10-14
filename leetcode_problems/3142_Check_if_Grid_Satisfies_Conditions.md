# 3142. Check if Grid Satisfies Conditions

Difficulty: easy

Link: https://leetcode.com/problems/check-if-grid-satisfies-conditions/

Contains PNG: Yes

PNG Links:
- https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png
- https://assets.leetcode.com/uploads/2024/03/27/example21.png
- https://assets.leetcode.com/uploads/2024/03/31/changed.png

## Problem Statement

You are given a 2D matrix `grid` of size `m x n`. You need to check if each cell `grid[i][j]` is:

* Equal to the cell below it, i.e. `grid[i][j] == grid[i + 1][j]` (if it exists).
* Different from the cell to its right, i.e. `grid[i][j] != grid[i][j + 1]` (if it exists).

Return `true` if **all** the cells satisfy these conditions, otherwise, return `false`.

**Example 1:**

**Input:** grid \= \[\[1,0,2],\[1,0,2]]

**Output:** true

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/04/15/examplechanged.png)**

All the cells in the grid satisfy the conditions.

**Example 2:**

**Input:** grid \= \[\[1,1,1],\[0,0,0]]

**Output:** false

**Explanation:**

**![](https://assets.leetcode.com/uploads/2024/03/27/example21.png)**

All cells in the first row are equal.

**Example 3:**

**Input:** grid \= \[\[1],\[2],\[3]]

**Output:** false

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/03/31/changed.png)

Cells in the first column have different values.

**Constraints:**

* `1 <= n, m <= 10`
* `0 <= grid[i][j] <= 9`

## Hints

- 1\. Check if each column has same value in each cell.
- 2\. If the previous condition is satisfied, we can simply check the first cells in adjacent columns.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    bool satisfiesConditions(vector<vector<int>>& grid) {
        
    }
};
```

### Java
```java
class Solution {
    public boolean satisfiesConditions(int[][] grid) {
        
    }
}
```

### Python
```python
class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:
        
```

