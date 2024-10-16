# 3195. Find the Minimum Area to Cover All Ones I

Difficulty: medium

Link: https://leetcode.com/problems/find-the-minimum-area-to-cover-all-ones-i/

Contains PNG: Yes

PNG Links:
- https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png
- https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png

## Problem Statement

You are given a 2D **binary** array `grid`. Find a rectangle with horizontal and vertical sides with the **smallest** area, such that all the 1's in `grid` lie inside this rectangle.

Return the **minimum** possible area of the rectangle.

**Example 1:**

**Input:** grid \= \[\[0,1,0],\[1,0,1]]

**Output:** 6

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/08/examplerect0.png)

The smallest rectangle has a height of 2 and a width of 3, so it has an area of `2 * 3 = 6`.

**Example 2:**

**Input:** grid \= \[\[1,0],\[0,0]]

**Output:** 1

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/05/08/examplerect1.png)

The smallest rectangle has both height and width 1, so its area is `1 * 1 = 1`.

**Constraints:**

* `1 <= grid.length, grid[i].length <= 1000`
* `grid[i][j]` is either 0 or 1\.
* The input is generated such that there is at least one 1 in `grid`.

## Hints

- 1\. Find the minimum and maximum coordinates of a cell with a value of 1 in both directions.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minimumArea(vector<vector<int>>& grid) {
        
    }
};
```

### Java
```java
class Solution {
    public int minimumArea(int[][] grid) {
        
    }
}
```

### Python
```python
class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        
```

