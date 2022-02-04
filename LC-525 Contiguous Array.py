"""
Given a binary array nums, return the maximum length of a contiguous subarray with an 
equal number of 0 and 1.

Example 1:
Input: nums = [0, 1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.

Example 2:
Input: nums = [0, 1, 0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.
"""


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix_sum_arr = []
        prefix_sum_dict = {}
        curr_prefix_sum = 0
        # create a dict that contains prefix sum value as keys with values
        # being the highest index with that sum value
        for i in range(0, len(nums)):
            if nums[i] > 0:
                curr_prefix_sum += 1
            else:
                curr_prefix_sum -= 1

            prefix_sum_dict[curr_prefix_sum] = i
            prefix_sum_arr.append(curr_prefix_sum)

        # loop through and for each value find
        max_length_found = 0
        for j in range(0, len(nums)):
            # if it's a 1 we want it's prefix sum -1
            offset = -1
            # if it's a 0 we want it's prefix sum +1
            if nums[j] == 0:
                offset = 1

            arr_length = 0
            # get the dict entry for prefix_sum of current_sum + offset
            matching_sum = prefix_sum_dict.get(prefix_sum_arr[j]+offset)

            if(matching_sum):
                arr_length = matching_sum - j + 1

            max_length_found = max(arr_length, max_length_found)

        return max_length_found
