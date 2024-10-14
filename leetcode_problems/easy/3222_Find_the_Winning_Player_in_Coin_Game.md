# 3222. Find the Winning Player in Coin Game

Difficulty: easy

Link: https://leetcode.com/problems/find-the-winning-player-in-coin-game/

## Problem Statement

You are given two **positive** integers `x` and `y`, denoting the number of coins with values 75 and 10 *respectively*.

Alice and Bob are playing a game. Each turn, starting with **Alice**, the player must pick up coins with a **total** value 115\. If the player is unable to do so, they **lose** the game.

Return the *name* of the player who wins the game if both players play **optimally**.

**Example 1:**

**Input:** x \= 2, y \= 7

**Output:** "Alice"

**Explanation:**

The game ends in a single turn:

* Alice picks 1 coin with a value of 75 and 4 coins with a value of 10\.

**Example 2:**

**Input:** x \= 4, y \= 11

**Output:** "Bob"

**Explanation:**

The game ends in 2 turns:

* Alice picks 1 coin with a value of 75 and 4 coins with a value of 10\.
* Bob picks 1 coin with a value of 75 and 4 coins with a value of 10\.

**Constraints:**

* `1 <= x, y <= 100`

## Hints

- 1\. The only way to make 115 is to use one coin of value 75 and four coins of value 10\. Each turn uses up these many coins.
- 2\. Hence the number of turns is `min(x, y / 4)`.
- 3\. Determine the winner from its parity.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    string losingPlayer(int x, int y) {
        
    }
};
```

### Java
```java
class Solution {
    public String losingPlayer(int x, int y) {
        
    }
}
```

### Python
```python
class Solution:
    def losingPlayer(self, x: int, y: int) -> str:
        
```

