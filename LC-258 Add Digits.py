"""
Given an integer num, repeatedly add all its 
digits until the result has only one digit, 
and return it.

Example 1:
Input: num = 38
Output: 2
Explanation: The process is
38 - -> 3 + 8 - -> 11
11 - -> 1 + 1 - -> 2
Since 2 has only one digit, return it.

Example 2:
Input: num = 0
Output: 0
"""

class Solution:
    def addDigits(self, num: int) -> int:
        add_digits_num = num
        count = 0

        while len(str(add_digits_num)) > 1:
            for digit in str(add_digits_num):
                count += int(digit)

            add_digits_num = count
            count = 0

        return add_digits_num


""" O(1) solution
if num < 10:
    return num

return 9 if num % 9 == 0 else num % 9
"""
