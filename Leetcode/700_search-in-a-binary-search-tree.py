#
# @lc app=leetcode id=700 lang=python3
#
# [700] Search in a Binary Search Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if root is None:
            return None
        if root.val == val:
            return root
        nextroot1 = self.searchBST(root.left, val)
        if nextroot1:
            return nextroot1
        nextroot2 = self.searchBST(root.right, val)
        if nextroot2:
            return nextroot2
# @lc code=end
