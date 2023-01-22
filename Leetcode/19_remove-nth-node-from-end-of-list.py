#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> Optional[ListNode]:
        size = 0
        cur = head
        while cur:
            cur = cur.next
            size += 1
        idx = size - n
        cur2 = head
        temp = head
        while idx > 0:
            temp = cur2
            cur2 = cur2.next
            idx -= 1
        temp.next = cur2.next
        cur2.next = None
        return head


# @lc code=end
