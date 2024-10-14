# 3200. Maximum Height of a Triangle

Difficulty: easy

Link: https://leetcode.com/problems/maximum-height-of-a-triangle/

Contains PNG: Yes

PNG Links:
- https://assets.leetcode.com/uploads/2024/06/16/brb.png
- https://assets.leetcode.com/uploads/2024/06/16/br.png
- https://assets.leetcode.com/uploads/2024/06/16/br.png

## Problem Statement

You are given two integers `red` and `blue` representing the count of red and blue colored balls. You have to arrange these balls to form a triangle such that the 1st row will have 1 ball, the 2nd row will have 2 balls, the 3rd row will have 3 balls, and so on.

All the balls in a particular row should be the **same** color, and adjacent rows should have **different** colors.

Return the **maximum** *height of the triangle* that can be achieved.

**Example 1:**

**Input:** red \= 2, blue \= 4

**Output:** 3

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/brb.png)

The only possible arrangement is shown above.

**Example 2:**

**Input:** red \= 2, blue \= 1

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/br.png)  

The only possible arrangement is shown above.

**Example 3:**

**Input:** red \= 1, blue \= 1

**Output:** 1

**Example 4:**

**Input:** red \= 10, blue \= 1

**Output:** 2

**Explanation:**

![](https://assets.leetcode.com/uploads/2024/06/16/br.png)  

The only possible arrangement is shown above.

**Constraints:**

* `1 <= red, blue <= 100`

## Hints

- 1\. Count the max height using both possibilities. That is, red ball as top and blue ball as top.
- 2\. For counting the max height, use a simple for loop and remove the number of balls required at this level.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int maxHeightOfTriangle(int red, int blue) {
        
    }
};
```

### Java
```java
class Solution {
    public int maxHeightOfTriangle(int red, int blue) {
        
    }
}
```

### Python
```python
class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        
```

