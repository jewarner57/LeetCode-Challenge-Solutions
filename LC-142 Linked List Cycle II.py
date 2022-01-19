"""
Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

Do not modify the linked list.

https://leetcode.com/problems/linked-list-cycle-ii/
"""

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nodeList = []
        curr = head
        # traverse and store each node object in an array or dictionary
        # check that each node isnt already in the dictionary.
        while not curr in nodeList and curr is not None:
            nodeList.append(curr)
            curr = curr.next

        if curr is None:
            return None

        # if it is then return its index
        return nodeList[nodeList.index(curr)]
