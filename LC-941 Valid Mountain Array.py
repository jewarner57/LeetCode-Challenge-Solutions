"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Example 1:
Input: arr = [2,1]
Output: false

Example 2:
Input: arr = [3,5,5]
Output: false

Example 3:
Input: arr = [0,3,2,1]
Output: true
"""


class Solution(object):
    def validMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """

        # have a pointer that keeps track of inc or dec
        isIncreasing = True
        hasIncreased = False
        hasDecreased = False

        for i in range(0, len(arr)-1):
            # have we increased yet
            if not hasDecreased and arr[i] < arr[i+1]:
                hasIncreased = True
            # have we decreased yet
            if hasIncreased and arr[i] > arr[i+1]:
                hasDecreased = True

            # if a value is less than the prev val switch to dec
            if isIncreasing and not arr[i] < arr[i+1]:
                isIncreasing = False
            # if value doesnt match inc/dec pattern return false
            if (not isIncreasing and not arr[i] > arr[i+1]) or (arr[i] == arr[i+1]):
                return False
        return hasDecreased and hasIncreased
