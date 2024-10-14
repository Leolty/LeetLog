# 3196. Maximize Total Cost of Alternating Subarrays

Difficulty: medium

Link: https://leetcode.com/problems/maximize-total-cost-of-alternating-subarrays/

Contains PNG: No

## Problem Statement

You are given an integer array `nums` with length `n`.

The **cost** of a subarray `nums[l..r]`, where `0 <= l <= r < n`, is defined as:

`cost(l, r) = nums[l] - nums[l + 1] + ... + nums[r] * (−1)r − l`

Your task is to **split** `nums` into subarrays such that the **total** **cost** of the subarrays is **maximized**, ensuring each element belongs to **exactly one** subarray.

Formally, if `nums` is split into `k` subarrays, where `k > 1`, at indices `i1, i2, ..., ik − 1`, where `0 <= i1 < i2 < ... < ik - 1 < n - 1`, then the total cost will be:

`cost(0, i1) + cost(i1 + 1, i2) + ... + cost(ik − 1 + 1, n − 1)`

Return an integer denoting the *maximum total cost* of the subarrays after splitting the array optimally.

**Note:** If `nums` is not split into subarrays, i.e. `k = 1`, the total cost is simply `cost(0, n - 1)`.

**Example 1:**

**Input:** nums \= \[1,\-2,3,4]

**Output:** 10

**Explanation:**

One way to maximize the total cost is by splitting `[1, -2, 3, 4]` into subarrays `[1, -2, 3]` and `[4]`. The total cost will be `(1 + 2 + 3) + 4 = 10`.

**Example 2:**

**Input:** nums \= \[1,\-1,1,\-1]

**Output:** 4

**Explanation:**

One way to maximize the total cost is by splitting `[1, -1, 1, -1]` into subarrays `[1, -1]` and `[1, -1]`. The total cost will be `(1 + 1) + (1 + 1) = 4`.

**Example 3:**

**Input:** nums \= \[0]

**Output:** 0

**Explanation:**

We cannot split the array further, so the answer is 0\.

**Example 4:**

**Input:** nums \= \[1,\-1]

**Output:** 2

**Explanation:**

Selecting the whole array gives a total cost of `1 + 1 = 2`, which is the maximum.

**Constraints:**

* `1 <= nums.length <= 105`
* `-109 <= nums[i] <= 109`

## Hints

- 1\. The problem can be solved using dynamic programming.
- 2\. Since we can always start a new subarray, the problem is the same as selecting some elements in the array and flipping their signs to negative to maximize the sum. However, we cannot flip the signs of 2 consecutive elements, and the first element in the array cannot be negative.
- 3\. Let `dp[i][0/1]` be the largest sum we can get for prefix `nums[0..i]`, where `dp[i][0]` is the maximum if the `ith` element wasn't flipped, and `dp[i][1]` is the maximum if the `ith` element was flipped.
- 4\. Based on the restriction:
- 
- `dp[i][0] = max(dp[i - 1][0], dp[i - 1][1]) + nums[i]`
- 
- `dp[i][1] = dp[i - 1][0] - nums[i]`
- 5\. The initial state is:
- 
- `dp[1][0] = nums[0] + nums[1]`
- 
- `dp[1][1] = nums[0] - nums[1]`
- 
- and the answer is `max(dp[n - 1][0], dp[n - 1][1])`.
- 6\. Can you optimize the space complexity?

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long maximumTotalCost(vector<int>& nums) {
        
    }
};
```

### Java
```java
class Solution {
    public long maximumTotalCost(int[] nums) {
        
    }
}
```

### Python
```python
class Solution:
    def maximumTotalCost(self, nums: List[int]) -> int:
        
```

