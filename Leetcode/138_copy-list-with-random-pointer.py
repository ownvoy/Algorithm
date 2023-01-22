#
# @lc app=leetcode id=138 lang=python3
#
# [138] Copy List with Random Pointer
#

# @lc code=start
"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        val_list = []
        ran_list = []
        cur = head
        while cur:
            val_list.append(cur.val)
            ran_list.append(cur.random)
            cur = cur.next
        dummy = Node(1000000)
        cur = dummy

        for i in val_list:
            cur.next = Node(i)
            cur = cur.next
        dhead = dummy.next
        dummy.next = None

        cur = dhead
        temp = head
        list_map = {}

        while temp:
            list_map[temp] = cur
            temp = temp.next
            cur = cur.next

        cur = dhead
        while node in ran_list:
            cur.random = list_map[node]
            cur = cur.next

        return dhead


# @lc code=end
