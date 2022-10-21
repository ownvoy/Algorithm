# @before-stub-for-debug-begin
from typing import *

from python3problem104 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=104 lang=python3
#
# [104] Maximum Depth of Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self.depth = {}
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        if len(self.depth) == 0:
            self.depth[root] = 1
        if root.left is not None:
            self.depth[root.left] = self.depth[root] + 1
            self.maxDepth(root.left)
        if root.right is not None:
            self.depth[root.right] = self.depth[root] + 1
            self.maxDepth(root.right)
        return max(self.depth.values())
# @lc code=end
