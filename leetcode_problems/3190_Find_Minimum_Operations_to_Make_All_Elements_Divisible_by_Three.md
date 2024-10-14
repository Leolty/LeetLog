# 3190. Find Minimum Operations to Make All Elements Divisible by Three

Difficulty: easy

Link: https://leetcode.com/problems/find-minimum-operations-to-make-all-elements-divisible-by-three/

Contains PNG: No

## Problem Statement

You are given an integer array `nums`. In one operation, you can add or subtract 1 from **any** element of `nums`.

Return the **minimum** number of operations to make all elements of `nums` divisible by 3\.

**Example 1:**

**Input:** nums \= \[1,2,3,4]

**Output:** 3

**Explanation:**

All array elements can be made divisible by 3 using 3 operations:

* Subtract 1 from 1\.
* Add 1 to 2\.
* Subtract 1 from 4\.

**Example 2:**

**Input:** nums \= \[3,6,9]

**Output:** 0

**Constraints:**

* `1 <= nums.length <= 50`
* `1 <= nums[i] <= 50`

## Hints

- 1\. If `x % 3 != 0` we can always increment or decrement `x` such that we only need 1 operation.
- 2\. Add `min(nums[i] % 3, 3 - (num[i] % 3))` to the count of operations.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minimumOperations(vector<int>& nums) {
        
    }
};
```

### Java
```java
class Solution {
    public int minimumOperations(int[] nums) {
        
    }
}
```

### Python
```python
class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
```

