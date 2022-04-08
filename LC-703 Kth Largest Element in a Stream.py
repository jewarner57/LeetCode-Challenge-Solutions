"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element in the sorted order, not the kth distinct element.

Implement KthLargest class:

KthLargest(int k, int[] nums) Initializes the object with the integer k and the stream of integers nums.
int add(int val) Appends the integer val to the stream and returns the element representing the kth largest element in the stream.
 

Example 1:

Input
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
Output
[null, 4, 5, 5, 8, 8]

Explanation
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8


had problems understanding the problem. It feels very poorly layed out. If I had had a live person to ask questions about the problem before hand I could have had a much easier time of solving this. The example given is also very poor. Good question for an interview, bad question for Leetcode"
"""

class KthLargest:

    def __init__(self, k: int, nums: List[int]): 
        self.k = k
        self.nums = nums

    def add(self, val: int) -> int:
        streamNums = self.nums
        streamNums.append(val)
        streamNums.sort()
        return streamNums[-self.k]
