
# @before-stub-for-debug-begin
from typing import *

from python3problem143 import *

# @before-stub-for-debug-end

#
# @lc app=leetcode id=143 lang=python3
#
# [143] Reorder List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = nextinit

class Solution:
    def reorderList(self, head) -> None:
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        div_head = slow.next
        slow.next = None
        if div_head:
            rev_div_head = self.reverse(div_head)
            self.merge(head, rev_div_head)

    def reverse(self, head):
        first = head
        second = head.next
        first.next = None
        while second is not None:
            temp = second.next
            second.next = first
            first, second = second, temp
        return first

    def merge(self, head1, head2):
        cur1 = head1
        cur2 = head2
        while cur2 is not None:
            temp1 = cur1.next
            temp2 = cur2.next
            cur1.next = cur2
            cur2.next = temp1
            cur1 = temp1
            cur2 = temp2

# @lc code=end
