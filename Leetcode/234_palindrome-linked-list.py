# @before-stub-for-debug-begin
from python3problem234 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        cur = head
        copy = None
        while cur:
            if copy is None:
                copy = ListNode(cur.val)
                cur = cur.next
            else:
                newNode = ListNode(cur.val)
                newNode.next = copy
                copy = newNode
                cur = cur.next
        while copy:
            if copy.val != head.val:
                return False
            else:
                copy = copy.next
                head = head.next
        return True

# @lc code=end

