from typing import List

"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}
        for i, n in enumerate(nums):
            delta = target - n
            if delta in prev_map:
                return [prev_map[delta], i]
            prev_map[n] = i


class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = self._build_prev_map(nums)
        return self._find_indices(nums, target, prev_map)

    def _build_prev_map(self, nums: List[int]) -> dict:
        prev_map = {}
        for i, n in enumerate(nums):
            prev_map[n] = i
        return prev_map

    def _find_indices(self, nums: List[int], target: int, prev_map: dict) -> List[int]:
        for i, n in enumerate(nums):
            delta = target - n
            if delta in prev_map and prev_map[delta] != i:
                return [prev_map[delta], i]


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
