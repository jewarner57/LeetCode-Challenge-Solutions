"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
typically using all the original letters exactly once.

Example 1:
Input: s = "cbaebabacd", p = "abc"
Output: [0, 6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Example 2:
Input: s = "abab", p = "ab"
Output: [0, 1, 2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
"""


class Solution:
    # Sliding Window Solution
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # make a dict of all chars and their counts for p
        phraseDict = {}
        anagramDict = {}

        # add all lowercase english letters at 0
        for char in string.ascii_lowercase:
            phraseDict[char] = 0
            anagramDict[char] = 0

        # increment values for characters in p
        for char in p:
            phraseDict[char] += 1

        # setup for sliding window
        start = 0
        end = -1
        outputList = []

        # increment until the window reaches the end
        while end < len(s)-1:

            # dont increase start until end-start = len(p)
            if(end - start >= len(p)-1):
                # remove start char from the dict then increase start by one
                anagramDict[s[start]] -= 1
                start += 1

            # increment end and the value of the new letter
            end += 1
            anagramDict[s[end]] += 1

            # do the letter counts match?
            if anagramDict == phraseDict:
                # if so then add start to output list
                outputList.append(start)

        return outputList
