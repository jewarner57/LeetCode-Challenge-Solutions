"""
Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

For example:

A -> 1
B -> 2
C -> 3
...
Z -> 26
AA -> 27
AB -> 28 
...
 

Example 1:

Input: columnTitle = "A"
Output: 1
Example 2:

Input: columnTitle = "AB"
Output: 28
Example 3:

Input: columnTitle = "ZY"
Output: 701
"""

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        column_number = (ord(columnTitle[len(columnTitle)-1].lower()) - 96)

        for i in range(0, len(columnTitle)-1):
            place = len(columnTitle) - i - 1

            column_number += (ord(columnTitle[i].lower()) - 96) * (26 ** place)
            print(place)

        return column_number
