# @before-stub-for-debug-begin
from typing import *

from python3problem206 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head  or not head.next:
            return head
        lastnode = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return lastnode
# @lc code=end

