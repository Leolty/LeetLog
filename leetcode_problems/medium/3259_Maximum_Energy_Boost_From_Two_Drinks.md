# 3259. Maximum Energy Boost From Two Drinks

Difficulty: medium

Link: https://leetcode.com/problems/maximum-energy-boost-from-two-drinks/

## Problem Statement

You are given two integer arrays `energyDrinkA` and `energyDrinkB` of the same length `n` by a futuristic sports scientist. These arrays represent the energy boosts per hour provided by two different energy drinks, A and B, respectively.

You want to *maximize* your total energy boost by drinking one energy drink *per hour*. However, if you want to switch from consuming one energy drink to the other, you need to wait for *one hour* to cleanse your system (meaning you won't get any energy boost in that hour).

Return the **maximum** total energy boost you can gain in the next `n` hours.

**Note** that you can start consuming *either* of the two energy drinks.

**Example 1:**

**Input:** energyDrinkA \= \[1,3,1], energyDrinkB \= \[3,1,1]

**Output:** 5

**Explanation:**

To gain an energy boost of 5, drink only the energy drink A (or only B).

**Example 2:**

**Input:** energyDrinkA \= \[4,1,1], energyDrinkB \= \[1,1,3]

**Output:** 7

**Explanation:**

To gain an energy boost of 7:

* Drink the energy drink A for the first hour.
* Switch to the energy drink B and we lose the energy boost of the second hour.
* Gain the energy boost of the drink B in the third hour.

**Constraints:**

* `n == energyDrinkA.length == energyDrinkB.length`
* `3 <= n <= 105`
* `1 <= energyDrinkA[i], energyDrinkB[i] <= 105`

## Hints

- 1\. Can we solve it using dynamic programming?
- 2\. Define `dpA[i]` as the maximum energy boost if we consider only the first `i + 1` hours such that in the last hour, we drink the energy drink A.
- 3\. Similarly define `dpB[i]`.
- 4\. `dpA[i] = max(dpA[i - 1], dpB[i - 2]) + energyDrinkA[i]`
- 5\. Similarly, fill `dpB`.
- 6\. The answer is `max(dpA[n - 1], dpB[n - 1])`.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    long long maxEnergyBoost(vector<int>& energyDrinkA, vector<int>& energyDrinkB) {
        
    }
};
```

### Java
```java
class Solution {
    public long maxEnergyBoost(int[] energyDrinkA, int[] energyDrinkB) {
        
    }
}
```

### Python
```python
class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
```

