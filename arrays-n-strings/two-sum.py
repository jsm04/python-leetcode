"""
Two Integer Sum
Given an array of integers nums and an integer target, return the indices i and j such that nums[i] + nums[j] == target and i != j.

You may assume that every input has exactly one pair of indices i and j that satisfy the condition.

Return the answer with the smaller index first.
"""


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        store: dict[int, int] = {}
        for i, n in enumerate(nums):
            # delta -> difference or change between two states or values
            # here delta is the complement necesary to get the target
            complement = target - n
            # if complement is stored in map return solution as index list
            if complement in store:
                return [store[complement], i]
            # stores number and index key pair in map
            store[n] = i
        return []


s = Solution()
# Executable examples:
nums1 = [3, 4, 5, 6]
target1 = 7
result1 = s.twoSum(nums1, target1)
print(f"Input: nums = {nums1}, target = {target1}, Output: {result1}")  # Output: [0, 1]

nums2 = [4, 5, 6]
target2 = 10
result2 = s.twoSum(nums2, target2)
print(f"Input: nums = {nums2}, target = {target2}, Output: {result2}")  # Output: [0, 2]

nums3 = [5, 5]
target3 = 10
result3 = s.twoSum(nums3, target3)
print(f"Input: nums = {nums3}, target = {target3}, Output: {result3}")  # Output: [0, 1]

nums4 = [1, 2, 3, 4, 5]
target4 = 9
result4 = s.twoSum(nums4, target4)
print(f"Input: nums = {nums4}, target = {target4}, Output: {result4}")  # output: [3,4]

nums5 = [3, 3]
target5 = 6
result5 = s.twoSum(nums5, target5)
print(f"Input: nums = {nums5}, target = {target5}, Output: {result5}")  # output: [0,1]
