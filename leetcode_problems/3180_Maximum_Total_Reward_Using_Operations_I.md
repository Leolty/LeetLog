# 3180. Maximum Total Reward Using Operations I

Difficulty: medium

Link: https://leetcode.com/problems/maximum-total-reward-using-operations-i/

Contains PNG: No

## Problem Statement

You are given an integer array `rewardValues` of length `n`, representing the values of rewards.

Initially, your total reward `x` is 0, and all indices are **unmarked**. You are allowed to perform the following operation **any** number of times:

* Choose an **unmarked** index `i` from the range `[0, n - 1]`.
* If `rewardValues[i]` is **greater** than your current total reward `x`, then add `rewardValues[i]` to `x` (i.e., `x = x + rewardValues[i]`), and **mark** the index `i`.

Return an integer denoting the **maximum** *total reward* you can collect by performing the operations optimally.

**Example 1:**

**Input:** rewardValues \= \[1,1,3,3]

**Output:** 4

**Explanation:**

During the operations, we can choose to mark the indices 0 and 2 in order, and the total reward will be 4, which is the maximum.

**Example 2:**

**Input:** rewardValues \= \[1,6,4,3,2]

**Output:** 11

**Explanation:**

Mark the indices 0, 2, and 1 in order. The total reward will then be 11, which is the maximum.

**Constraints:**

* `1 <= rewardValues.length <= 2000`
* `1 <= rewardValues[i] <= 2000`

## Hints

- 1\. Sort the rewards array first.
- 2\. If we decide to apply some rewards, it's always optimal to apply them in order.
- 3\. Let `dp[i][j]` (true/false) be the state after the first `i` rewards, indicating whether we can get exactly `j` points.
- 4\. The transition is given by: `dp[i][j] = dp[i - 1][j − rewardValues[i]]` if `j − rewardValues[i] < rewardValues[i]`.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int maxTotalReward(vector<int>& rewardValues) {
        
    }
};
```

### Java
```java
class Solution {
    public int maxTotalReward(int[] rewardValues) {
        
    }
}
```

### Python
```python
class Solution:
    def maxTotalReward(self, rewardValues: List[int]) -> int:
        
```

