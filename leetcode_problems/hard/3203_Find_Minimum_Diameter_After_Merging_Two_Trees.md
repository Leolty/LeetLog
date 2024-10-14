# 3203. Find Minimum Diameter After Merging Two Trees

Difficulty: hard

Link: https://leetcode.com/problems/find-minimum-diameter-after-merging-two-trees/

## Problem Statement

There exist two **undirected** trees with `n` and `m` nodes, numbered from `0` to `n - 1` and from `0` to `m - 1`, respectively. You are given two 2D integer arrays `edges1` and `edges2` of lengths `n - 1` and `m - 1`, respectively, where `edges1[i] = [ai, bi]` indicates that there is an edge between nodes `ai` and `bi` in the first tree and `edges2[i] = [ui, vi]` indicates that there is an edge between nodes `ui` and `vi` in the second tree.

You must connect one node from the first tree with another node from the second tree with an edge.

Return the **minimum** possible **diameter** of the resulting tree.

The **diameter** of a tree is the length of the *longest* path between any two nodes in the tree.

**Example 1:**![](https://assets.leetcode.com/uploads/2024/04/22/example11-transformed.png)

**Input:** edges1 \= \[\[0,1],\[0,2],\[0,3]], edges2 \= \[\[0,1]]

**Output:** 3

**Explanation:**

We can obtain a tree of diameter 3 by connecting node 0 from the first tree with any node from the second tree.

**Example 2:**

![](https://assets.leetcode.com/uploads/2024/04/22/example211.png)

**Input:** edges1 \= \[\[0,1],\[0,2],\[0,3],\[2,4],\[2,5],\[3,6],\[2,7]], edges2 \= \[\[0,1],\[0,2],\[0,3],\[2,4],\[2,5],\[3,6],\[2,7]]

**Output:** 5

**Explanation:**

We can obtain a tree of diameter 5 by connecting node 0 from the first tree with node 0 from the second tree.

**Constraints:**

* `1 <= n, m <= 105`
* `edges1.length == n - 1`
* `edges2.length == m - 1`
* `edges1[i].length == edges2[i].length == 2`
* `edges1[i] = [ai, bi]`
* `0 <= ai, bi < n`
* `edges2[i] = [ui, vi]`
* `0 <= ui, vi < m`
* The input is generated such that `edges1` and `edges2` represent valid trees.

## Hints

- 1\. Suppose that we connected node `a` in tree1 with node `b` in tree2\. The diameter length of the resulting tree will be the largest of the following 3 values:
- 1. The diameter of tree 1\.
- 2. The diameter of tree 2\.
- 3. The length of the longest path that starts at node `a` and that is completely within Tree 1 \+ The length of the longest path that starts at node `b` and that is completely within Tree 2 \+ 1\.
- 
- The added one in the third value is due to the additional edge that we have added between trees 1 and 2\.
- 2\. Values 1 and 2 are constant regardless of our choice of `a` and `b`. Therefore, we need to pick `a` and `b` in such a way that minimizes value 3\.
- 3\. If we pick `a` and `b` optimally, they will be in the diameters of Tree 1 and Tree 2, respectively. Exactly which nodes of the diameter should we pick?
- 4\. `a` is the center of the diameter of tree 1, and `b` is the center of the diameter of tree 2\.

## Code Templates

### Cpp
```cpp
class Solution {
public:
    int minimumDiameterAfterMerge(vector<vector<int>>& edges1, vector<vector<int>>& edges2) {
        
    }
};
```

### Java
```java
class Solution {
    public int minimumDiameterAfterMerge(int[][] edges1, int[][] edges2) {
        
    }
}
```

### Python
```python
class Solution:
    def minimumDiameterAfterMerge(self, edges1: List[List[int]], edges2: List[List[int]]) -> int:
        
```

