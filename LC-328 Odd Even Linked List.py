"""
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.
"""

class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head
        # get the length of the list
        length = 1
        node = head
        while node.next is not None:
            length += 1
            node = node.next
        # save the tail node of the list
        tail = node
        if head.next.next is None:
            return head
        # previous should be head
        previous = head
        # curr = head.next
        curr = head.next
        # keep a counter starting at 2
        counter = 2
        # while counter <= listlength
        while counter <= length:
            # add curr node to the end
            # save it’s .next, to next
            nextNode = curr.next
            # then set the tail’s .next to curr
            tail.next = curr
            # set the tail to curr
            tail = curr
            # set the curr’s .next to None
            tail.next = None
            # increase counter by 1
            counter += 1
            # splice the surrounding elements together
            # set the previous .next to the moved node’s .next (next)
            previous.next = nextNode
            curr = nextNode
            nextNode = curr.next
            # skip over it
            previous = curr
            curr = curr.next
            nextNode = curr.next
            counter += 1
            # # debugging thing
            # node = head
            # while node is not None:
            #     print(node.val)
            #     node = node.next
            # print()
        return head