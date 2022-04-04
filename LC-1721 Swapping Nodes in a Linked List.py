"""
https://leetcode.com/problems/swapping-nodes-in-a-linked-list/

You are given the head of a linked list, and an integer k.

Return the head of the linked list after swapping the values of the kth node from the beginning and the kth node from the end (the list is 1-indexed).

Example 1:
Input: head = [1,2,3,4,5], k = 2
Output: [1,4,3,2,5]

Example 2:
Input: head = [7,9,6,6,7,8,3,0,9,5], k = 5
Output: [7,9,6,6,8,7,3,0,9,5]
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        firstNode = None
        lastNode = None
        
        length = 0
        node = head
        while node is not None:
            length += 1
            node = node.next
        
        node = head
        firstIndex = k
        lastIndex = length - k + 1
        for i in range(1, length+1):
            if i == firstIndex:
                firstNode = node
            if i == lastIndex:
                lastNode = node
            node = node.next
        
        temp = firstNode.val
        firstNode.val = lastNode.val
        lastNode.val = temp
        
        return head
            
