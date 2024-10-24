from typing import List

"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map: dict[int, int] = {}
        for i, n in enumerate(nums):
            # delta -> difference or change between two states or values
            # here delta is the complement necesary to get the target
            complement = target - n
            # if complement is stored in map return solution as index list
            if complement in prev_map:
                return [prev_map[complement], i]
            # stores number and index key pair in map
            prev_map[n] = i
        return []


"""
Example 1:
Input:
nums = [3,4,5,6], target = 7
Output: [0,1]

Explanation: nums[0] + nums[1] == 7, so we return [0, 1].

Example 2:
Input: nums = [4,5,6], target = 10
Output: [0,2]
Example 3:

Input: nums = [5,5], target = 10
Output: [0,1]

Constraints:
-10,000,000 <= nums[i] <= 10,000,000
2 <= nums.length <= 1000
-10,000,000 <= target <= 10,000,000
"""
