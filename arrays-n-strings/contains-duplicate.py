from typing import List

"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""


class Solution:
    def contains_duplicate(self, nums: List[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


"""
Example 1:

Input: nums = [1, 2, 3, 3]

Output: true
Example 2:

Input: nums = [1, 2, 3, 4]

Output: false

"""
