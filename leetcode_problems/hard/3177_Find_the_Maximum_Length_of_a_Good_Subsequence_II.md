# 3177. Find the Maximum Length of a Good Subsequence II

Difficulty: hard

Link: https://leetcode.com/problems/find-the-maximum-length-of-a-good-subsequence-ii/

## Problem Statement

You are given an integer array `nums` and a **non\-negative** integer `k`. A sequence of integers `seq` is called **good** if there are **at most** `k` indices `i` in the range `[0, seq.length - 2]` such that `seq[i] != seq[i + 1]`.

Return the **maximum** possible length of a **good** subsequence of `nums`.

**Example 1:**

**Input:** nums \= \[1,2,1,1,3], k \= 2

**Output:** 4

**Explanation:**

The maximum length subsequence is `[1,2,1,1,3]`.

**Example 2:**

**Input:** nums \= \[1,2,3,4,5,1], k \= 0

**Output:** 2

**Explanation:**

The maximum length subsequence is `[1,2,3,4,5,1]`.

**Constraints:**

* `1 <= nums.length <= 5 * 103`
* `1 <= nums[i] <= 109`
* `0 <= k <= min(50, nums.length)`

## Hints

- 1\. The absolute values in `nums` don’t really matter. So we can remap the set of values to the range `[0, n - 1]`.
- 2\. Let `dp[i][j]` be the length of the longest subsequence till index `j` with at most `i` positions such that `seq[i] != seq[i + 1]`.
- 3\. For each value `x` from left to right, update `dp[i][x] = max(dp[i][x] + 1, dp[i - 1][y] + 1)`, where `y != x`.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int maximumLength(vector<int>& nums, int k) {
        
    }
};
```

### Java
```java
class Solution {
    public int maximumLength(int[] nums, int k) {
        
    }
}
```

### Python
```python
class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        
```

