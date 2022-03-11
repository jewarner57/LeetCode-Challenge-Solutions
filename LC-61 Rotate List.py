"""
Given the head of a linked list, rotate the list to the right by k places.

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]

Example 2:
Input: head = [0,1,2], k = 4
Output: [2,0,1]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head

        listlength = 1
        tail = head

        # get list length
        while tail.next is not None:
            listlength += 1
            tail = tail.next

        k = k % listlength
        if k < 1:
            return head

        newTail = head
        for _ in range(1, listlength - k):
            newTail = newTail.next

        newHead = newTail.next
        tail.next = head
        newTail.next = None

        return newHead
