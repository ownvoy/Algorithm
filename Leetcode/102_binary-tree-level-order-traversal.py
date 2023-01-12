#
# @lc app=leetcode id=102 lang=python3
#
# [102] Binary Tree Level Order Traversal
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = deque()
        levelMap = {}
        if root is None:
            return []
        queue.append(root)
        levelMap[root] = 0
        while queue:
            cur = queue.popleft()
            if cur.left:
                queue.append(cur.left)
                levelMap[cur.left] = levelMap[cur] + 1
            if cur.right:
                queue.append(cur.right)
                levelMap[cur.right] = levelMap[cur] + 1
        num = max(list(levelMap.values())) + 1
        result = []
        for _ in range(num):
            result.append([])
        for node, idx in levelMap.items():
            result[idx].append(node.val)
        return result


# @lc code=end
