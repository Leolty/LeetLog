# 3153. Sum of Digit Differences of All Pairs

Difficulty: medium

Link: https://leetcode.com/problems/sum-of-digit-differences-of-all-pairs/

Contains PNG: No

## Problem Statement

You are given an array `nums` consisting of **positive** integers where all integers have the **same** number of digits.

The **digit difference** between two integers is the *count* of different digits that are in the **same** position in the two integers.

Return the **sum** of the **digit differences** between **all** pairs of integers in `nums`.

**Example 1:**

**Input:** nums \= \[13,23,12]

**Output:** 4

**Explanation:**  

We have the following:  

\- The digit difference between **1**3 and **2**3 is 1\.  

\- The digit difference between 1**3** and 1**2** is 1\.  

\- The digit difference between **23** and **12** is 2\.  

So the total sum of digit differences between all pairs of integers is `1 + 1 + 2 = 4`.

**Example 2:**

**Input:** nums \= \[10,10,10,10]

**Output:** 0

**Explanation:**  

All the integers in the array are the same. So the total sum of digit differences between all pairs of integers will be 0\.

**Constraints:**

* `2 <= nums.length <= 105`
* `1 <= nums[i] < 109`
* All integers in `nums` have the same number of digits.

## Hints

- 1\. You can solve the problem for digits that are on the same position separately, and then sum up all the answers.
- 2\. For each position, count the number of occurences of each digit from 0 to 9 that appear on that position.
- 3\. Let `c` be the number of occurences of a digit on a position, that will contribute with `c * (n - c)` to the final answer, where `n` is the number of integers in `nums`.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long sumDigitDifferences(vector<int>& nums) {
        
    }
};
```

### Java
```java
class Solution {
    public long sumDigitDifferences(int[] nums) {
        
    }
}
```

### Python
```python
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        
```

