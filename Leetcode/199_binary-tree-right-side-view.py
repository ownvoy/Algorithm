# @before-stub-for-debug-begin
from python3problem199 import *
from typing import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=199 lang=python3
#
# [199] Binary Tree Right Side View
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
    def __init__(self) -> None:
        self.traversal = {}
        self.result = []

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return self.traversal
        queue = deque()
        level = 0
        queue.append((root, level))
        while queue:
            curnode, curlevel = queue.popleft()
            if curlevel not in self.traversal:
                self.traversal[curlevel] = [curnode.val]
            else:
                self.traversal[curlevel].append(curnode.val)
            if curnode.left:
                queue.append((curnode.left, curlevel + 1))
            if curnode.right:
                queue.append((curnode.right, curlevel + 1))
        for i in self.traversal.values():
            self.result.append(i[-1])
        return self.result


# @lc code=end
