"""
Given the root node of a binary search tree and two integers low and high, 
return the sum of values of all nodes with a value in the inclusive range [low, high].

Input: root = [10,5,15,3,7,null,18], low = 7, high = 15
Output: 32
Explanation: Nodes 7, 10, and 15 are in the range [7, 15]. 7 + 10 + 15 = 32.
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        
        self.SumBST(root, low, high)
        
        return self.sum
    
    def SumBST(self, root, low, high):
        if(root == None):
            return
        
        if(root.val >= low and root.val <= high):
            self.sum += root.val
        
        self.SumBST(root.left, low, high)
        self.SumBST(root.right, low, high)