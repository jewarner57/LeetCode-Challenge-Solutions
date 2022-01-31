"""
LC-189 Rotate Array

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]

"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def appendNode(self, node):
        if self.head is None:
            self.head = node
            return
        elif self.tail is None:
            self.head.next = node
            self.tail = node
            self.tail.prev = self.head
            return
        
        node.prev = self.tail
        self.tail.next = node
        self.tail = node
    
    def rotateList(self):
        if self.head is None:
            print('Head is None')
            return None
        elif self.tail is None:
            print('Tail is None')
            return self.head
        
        # move the tail to the head
        self.tail.next = self.head
        self.head.prev = self.tail
        self.head = self.tail
        self.tail = self.head.prev
        self.tail.next = None
        self.head.prev = None
    
    def printList(self):
        node = self.head
        while node is not None:
            node = node.next
    
    def toArray(self):
        node = self.head
        arr = []
        while node is not None:
            arr.append(node.val)
            node = node.next
        return arr
        
            
        
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # swap in place and move the whole array
            # cons - very slow On*n time
            # pros - o(1) space
            
        # put all data from nums into a doubly linked list then
        # complete all rotations
            # pros - O(n) time, O(2n) space
            # cons - gotta use a doubly linked list
        
        linked_list = LinkedList()
        for num in nums:
            linked_list.appendNode(Node(num))
            
        for i in range(0, k):
            linked_list.rotateList()
            
            
        arr = linked_list.toArray()
        print(arr, nums)
        for j in range(0, len(nums)):
            nums[j] = arr[j]