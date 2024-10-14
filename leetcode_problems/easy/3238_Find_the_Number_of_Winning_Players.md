# 3238. Find the Number of Winning Players

Difficulty: easy

Link: https://leetcode.com/problems/find-the-number-of-winning-players/

## Problem Statement

You are given an integer `n` representing the number of players in a game and a 2D array `pick` where `pick[i] = [xi, yi]` represents that the player `xi` picked a ball of color `yi`.

Player `i` **wins** the game if they pick **strictly more** than `i` balls of the **same** color. In other words,

* Player 0 wins if they pick any ball.
* Player 1 wins if they pick at least two balls of the *same* color.
* ...
* Player `i` wins if they pick at least`i + 1` balls of the *same* color.

Return the number of players who **win** the game.

**Note** that *multiple* players can win the game.

**Example 1:**

**Input:** n \= 4, pick \= \[\[0,0],\[1,0],\[1,0],\[2,1],\[2,1],\[2,0]]

**Output:** 2

**Explanation:**

Player 0 and player 1 win the game, while players 2 and 3 do not win.

**Example 2:**

**Input:** n \= 5, pick \= \[\[1,1],\[1,2],\[1,3],\[1,4]]

**Output:** 0

**Explanation:**

No player wins the game.

**Example 3:**

**Input:** n \= 5, pick \= \[\[1,1],\[2,4],\[2,4],\[2,4]]

**Output:** 1

**Explanation:**

Player 2 wins the game by picking 3 balls with color 4\.

**Constraints:**

* `2 <= n <= 10`
* `1 <= pick.length <= 100`
* `pick[i].length == 2`
* `0 <= xi <= n - 1`
* `0 <= yi <= 10`

## Hints

- 1\. Keep track of the number of balls of each color for each user using hashing.
- 2\. Find the maximum color that occurred for each player.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int winningPlayerCount(int n, vector<vector<int>>& pick) {
        
    }
};
```

### Java
```java
class Solution {
    public int winningPlayerCount(int n, int[][] pick) {
        
    }
}
```

### Python
```python
class Solution:
    def winningPlayerCount(self, n: int, pick: List[List[int]]) -> int:
        
```

