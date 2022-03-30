"""
Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.


Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # add all of the matrix sub arrays together into one large array.
        # do binary search on this new large array
        
        largeList = []
        
        for row in matrix:
            largeList += row
        
        first = 0
        last = len(largeList) - 1
            
        while first <= last:
            mid = (first + last) // 2
            if largeList[mid] == target:
                return True
            if target < largeList[mid]:
                last = mid - 1
            else:
                first = mid + 1
        
        return False
