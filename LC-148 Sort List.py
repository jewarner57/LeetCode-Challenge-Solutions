"""
Given the head of a linked list, return the list after sorting it in ascending order.

Sort a linked list in a ascending order
  * I used the slow / fast pointer method to get midpoint of
  linked list
  * I used merge sort to merge the lists back together
  correctly

https://leetcode.com/problems/sort-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.mergeSort(head)

    def mergeSort(self, head):

        if head is None or head.next is None:
            return head

        front, back = self.splitList(head)

        list1 = self.mergeSort(front)
        list2 = self.mergeSort(back)

        return self.mergeLists(list1, list2)

    def mergeLists(self, list1, list2):
        # Base cases
        if list1 is None:
            return list2
        if list2 is None:
            return list1

        if list1.val <= list2.val:
            result = list1
            result.next = self.mergeLists(list1.next, list2)
        else:
            result = list2
            result.next = self.mergeLists(list1, list2.next)

        return result

    def splitList(self, head):
        if head.next is None or head is None:
            front = head
            back = None
            return front, back

        slow = head
        fast = head.next

        while fast:
            fast = fast.next
            if fast:
                fast = fast.next
                slow = slow.next

        front = head
        back = slow.next
        slow.next = None

        return front, back
