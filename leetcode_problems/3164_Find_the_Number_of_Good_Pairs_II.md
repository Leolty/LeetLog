# 3164. Find the Number of Good Pairs II

Difficulty: medium

Link: https://leetcode.com/problems/find-the-number-of-good-pairs-ii/

Contains PNG: No

## Problem Statement

You are given 2 integer arrays `nums1` and `nums2` of lengths `n` and `m` respectively. You are also given a **positive** integer `k`.

A pair `(i, j)` is called **good** if `nums1[i]` is divisible by `nums2[j] * k` (`0 <= i <= n - 1`, `0 <= j <= m - 1`).

Return the total number of **good** pairs.

**Example 1:**

**Input:** nums1 \= \[1,3,4], nums2 \= \[1,3,4], k \= 1

**Output:** 5

**Explanation:**

The 5 good pairs are `(0, 0)`, `(1, 0)`, `(1, 1)`, `(2, 0)`, and `(2, 2)`.
**Example 2:**

**Input:** nums1 \= \[1,2,4,12], nums2 \= \[2,4], k \= 3

**Output:** 2

**Explanation:**

The 2 good pairs are `(3, 0)` and `(3, 1)`.

**Constraints:**

* `1 <= n, m <= 105`
* `1 <= nums1[i], nums2[j] <= 106`
* `1 <= k <= 103`

## Hints

- 1\. Let `f[v]` be the number of occurrences of `v/k` in nums2\.
- 2\. For each value `v` in nums1, enumerating all its factors `d` (in `sqrt(v)` time) and sum up all the `f[d]` to get the final answer.
- 3\. It is also possible to improve the complexity from `len(nums1) * sqrt(v)` to `len(nums1) * log(v)` \- How?

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long numberOfPairs(vector<int>& nums1, vector<int>& nums2, int k) {
        
    }
};
```

### Java
```java
class Solution {
    public long numberOfPairs(int[] nums1, int[] nums2, int k) {
        
    }
}
```

### Python
```python
class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
```

