# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque


class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        queue = deque()
        queue.append((root, 0))
        numlist = [0]
        while queue:
            node, level = queue.popleft()
            if node.left:
                queue.append((node.left, level + 1))
                numlist.append(level + 1)
            if node.right:
                queue.append((node.right, level + 1))
                numlist.append(level + 1)
        return max(numlist)
