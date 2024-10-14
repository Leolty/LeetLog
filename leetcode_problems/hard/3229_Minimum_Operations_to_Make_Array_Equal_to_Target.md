# 3229. Minimum Operations to Make Array Equal to Target

Difficulty: hard

Link: https://leetcode.com/problems/minimum-operations-to-make-array-equal-to-target/

## Problem Statement

You are given two positive integer arrays `nums` and `target`, of the same length.

In a single operation, you can select any subarray of `nums` and increment each element within that subarray by 1 or decrement each element within that subarray by 1\.

Return the **minimum** number of operations required to make `nums` equal to the array `target`.

**Example 1:**

**Input:** nums \= \[3,5,1,2], target \= \[4,6,2,4]

**Output:** 2

**Explanation:**

We will perform the following operations to make `nums` equal to `target`:  

\- Increment `nums[0..3]` by 1, `nums = [4,6,2,3]`.  

\- Increment `nums[3..3]` by 1, `nums = [4,6,2,4]`.

**Example 2:**

**Input:** nums \= \[1,3,2], target \= \[2,1,4]

**Output:** 5

**Explanation:**

We will perform the following operations to make `nums` equal to `target`:  

\- Increment `nums[0..0]` by 1, `nums = [2,3,2]`.  

\- Decrement `nums[1..1]` by 1, `nums = [2,2,2]`.  

\- Decrement `nums[1..1]` by 1, `nums = [2,1,2]`.  

\- Increment `nums[2..2]` by 1, `nums = [2,1,3]`.  

\- Increment `nums[2..2]` by 1, `nums = [2,1,4]`.

**Constraints:**

* `1 <= nums.length == target.length <= 105`
* `1 <= nums[i], target[i] <= 108`

## Hints

- 1\. Change `nums'[i] = nums[i] - target[i]`, so our goal is to make `nums'` into all 0s.
- 2\. Divide and conquer.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long minimumOperations(vector<int>& nums, vector<int>& target) {
        
    }
};
```

### Java
```java
class Solution {
    public long minimumOperations(int[] nums, int[] target) {
        
    }
}
```

### Python
```python
class Solution:
    def minimumOperations(self, nums: List[int], target: List[int]) -> int:
        
```

