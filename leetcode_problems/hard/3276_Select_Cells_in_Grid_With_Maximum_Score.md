# 3276. Select Cells in Grid With Maximum Score

Difficulty: hard

Link: https://leetcode.com/problems/select-cells-in-grid-with-maximum-score/

## Problem Statement

You are given a 2D matrix `grid` consisting of positive integers.

You have to select *one or more* cells from the matrix such that the following conditions are satisfied:

* No two selected cells are in the **same** row of the matrix.
* The values in the set of selected cells are **unique**.

Your score will be the **sum** of the values of the selected cells.

Return the **maximum** score you can achieve.

**Example 1:**

**Input:** grid \= \[\[1,2,3],\[4,3,2],\[1,1,1]]

**Output:** 8

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/29/grid1drawio.png)

We can select the cells with values 1, 3, and 4 that are colored above.

**Example 2:**

**Input:** grid \= \[\[8,7,6],\[8,3,2]]

**Output:** 15

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/07/29/grid8_8drawio.png)

We can select the cells with values 7 and 8 that are colored above.

**Constraints:**

* `1 <= grid.length, grid[i].length <= 10`
* `1 <= grid[i][j] <= 100`

## Hints

- 1\. Sort all the cells in the grid by their values and keep track of their original positions.
- 2\. Try dynamic programming with the following states: the current cell that we might select and a bitmask representing all the rows from which we have already selected a cell so far.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int maxScore(vector<vector<int>>& grid) {
        
    }
};
```

### Java
```java
class Solution {
    public int maxScore(List<List<Integer>> grid) {
        
    }
}
```

### Python
```python
class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        
```

