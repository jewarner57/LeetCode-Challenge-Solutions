"""
Given head which is a reference node to a singly-linked list. The value of each node in the linked list is either 0 or 1. The linked list holds the binary representation of a number.
Return the decimal value of the number in the linked list.

Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        # O(2n)
        # the length of the LL
        listLen = 0
        node = head
        while node is not None:
            listLen += 1
            node = node.next
        
        # then use that length to compute each value as you loop through the LL again
        node = head
        decimalVal = 0
        
        while node is not None:
            if node.val == 1:
                decimalVal += 2 ** (listLen-1)
            listLen -= 1
            node = node.next
        
        return decimalVal