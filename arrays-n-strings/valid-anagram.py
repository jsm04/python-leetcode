"""
Is Anagram
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.
"""


class Solution:
    """
    An anagram is a word or phrase formed by rearranging the letters of another word or phrase, using all the original letters exactly once.
    """

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        countS, countT = {}, {}

        for i, char in enumerate(s):
            # stores each char ocurrences in two separate dictionaries
            countS[char] = 1 + countS.get(char, 0)
            countT[t[i]] = 1 + countT.get(t[i], 0)

        # perform the check
        return countS == countT


s = "jar"
t = "jam"
s = Solution().isAnagram(s, t)
print(s)

"""
Example 1:
Input: s = "racecar", t = "carrace"
Output: true

Example 2:
Input: s = "jar", t = "jam"
Output: false

Constraints:
s and t consist of lowercase English letters.
"""
