"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

Example 1:
Input: head = [1,2,3,4]
Output: [2,1,4,3]

Example 2:
Input: head = []
Output: []

Example 3:
Input: head = [1]
Output: [1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if head is None or head.next is None:
            return head

        # For swapping the first two elements
        old_head = head
        head = head.next
        pair_adjacent_node = head.next
        old_head.next = pair_adjacent_node
        head.next = old_head

        prev_node = head.next
        first_node = pair_adjacent_node

        while first_node is not None and first_node.next is not None:
            new_first = first_node.next
            pair_adjacent_node = new_first.next
            new_first.next = first_node
            first_node.next = pair_adjacent_node
            prev_node.next = new_first

            prev_node = first_node
            first_node = pair_adjacent_node

        return head

        # first nodes next should be node.next.next
        # second node's next should be first node
        # node before first's next should be second
