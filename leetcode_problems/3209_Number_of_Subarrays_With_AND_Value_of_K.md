# 3209. Number of Subarrays With AND Value of K

Difficulty: hard

Link: https://leetcode.com/problems/number-of-subarrays-with-and-value-of-k/

Contains PNG: No

## Problem Statement

Given an array of integers `nums` and an integer `k`, return the number of subarrays of `nums` where the bitwise `AND` of the elements of the subarray equals `k`.

**Example 1:**

**Input:** nums \= \[1,1,1], k \= 1

**Output:** 6

**Explanation:**

All subarrays contain only 1's.

**Example 2:**

**Input:** nums \= \[1,1,2], k \= 1

**Output:** 3

**Explanation:**

Subarrays having an `AND` value of 1 are: `[1,1,2]`, `[1,1,2]`, `[1,1,2]`.

**Example 3:**

**Input:** nums \= \[1,2,3], k \= 2

**Output:** 2

**Explanation:**

Subarrays having an `AND` value of 2 are: `[1,2,3]`, `[1,2,3]`.

**Constraints:**

* `1 <= nums.length <= 105`
* `0 <= nums[i], k <= 109`

## Hints

- 1\. Let’s say we want to count the number of pairs `(l, r)` such that `nums[l] & nums[l + 1] & … & nums[r] == k`.
- 2\. Fix the left index `l`.
- 3\. Note that if you increase `r` for a fixed `l`, then the AND value of the subarray either decreases or remains unchanged.
- 4\. Therefore, consider using binary search.
- 5\. To calculate the AND value of a subarray, use sparse tables.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long countSubarrays(vector<int>& nums, int k) {
        
    }
};
```

### Java
```java
class Solution {
    public long countSubarrays(int[] nums, int k) {
        
    }
}
```

### Python
```python
class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        
```

