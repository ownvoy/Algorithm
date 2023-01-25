#
# @lc app=leetcode id=1448 lang=python3
#
# [1448] Count Good Nodes in Binary Tree
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        stack = [(root, root.val)]
        result = 1
        while stack:
            node, val = stack.pop()
            if node.left:
                if val <= node.left.val:
                    result += 1
                    stack.append((node.left, node.left.val))
                else:
                    stack.append((node.left, val))
            if node.right:
                if val <= node.right.val:
                    result += 1
                    stack.append((node.right, node.right.val))
                else:
                    stack.append((node.right, val))
        return result


# @lc code=end
