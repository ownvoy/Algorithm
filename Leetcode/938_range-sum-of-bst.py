#
# @lc app=leetcode id=938 lang=python3
#
# [938] Range Sum of BST
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import Counter


class Solution:
    def __init__(self):
        self.result1 = []

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.traversal_high(root, high)
        self.traversal_low(root, low)
        counter = Counter(self.result1)
        result = 0
        for key, value in counter.items():
            if value == 2:
                result += key

        return result

    def traversal_low(self, root, low):
        if root is None:
            return
        self.traversal_low(root.left, low)

        if root is not None and root.val >= low:
            self.result1.append(root.val)
        if root is None:
            return
        self.traversal_low(root.right, low)

    def traversal_high(self, root, high):
        if root is None:
            return
        self.traversal_high(root.left, high)

        if root is not None and root.val <= high:
            self.result1.append(root.val)
        self.traversal_high(root.right, high)


# @lc code=end
