# 3301. Maximize the Total Height of Unique Towers

Difficulty: medium

Link: https://leetcode.com/problems/maximize-the-total-height-of-unique-towers/

Contains PNG: No

## Problem Statement

You are given an array `maximumHeight`, where `maximumHeight[i]` denotes the **maximum** height the `ith` tower can be assigned.

Your task is to assign a height to each tower so that:

1. The height of the `ith` tower is a positive integer and does not exceed `maximumHeight[i]`.
2. No two towers have the same height.

Return the **maximum** possible total sum of the tower heights. If it's not possible to assign heights, return `-1`.

**Example 1:**

**Input:** maximumHeight \= \[2,3,4,3]

**Output:** 10

**Explanation:**

We can assign heights in the following way: `[1, 2, 4, 3]`.

**Example 2:**

**Input:** maximumHeight \= \[15,10]

**Output:** 25

**Explanation:**

We can assign heights in the following way: `[15, 10]`.

**Example 3:**

**Input:** maximumHeight \= \[2,2,1]

**Output:** \-1

**Explanation:**

It's impossible to assign positive heights to each index so that no two towers have the same height.

**Constraints:**

* `1 <= maximumHeight.length <= 105`
* `1 <= maximumHeight[i] <= 109`

## Hints

- 1\. Sort the array `maximumHeight` in descending order.
- 2\. After sorting, it can be seen that the maximum height that we can assign to the `ith` element is `min(maximumHeight[i], maximumHeight[i - 1] - 1)`.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long maximumTotalSum(vector<int>& maximumHeight) {
        
    }
};
```

### Java
```java
class Solution {
    public long maximumTotalSum(int[] maximumHeight) {
        
    }
}
```

### Python
```python
class Solution:
    def maximumTotalSum(self, maximumHeight: List[int]) -> int:
        
```

