"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
Return k.

Constraints:
1 <= nums.length <= 3 * 104
-100 <= nums[i] <= 100
nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        unique_nums = set()
        i = 0
        while i < len(nums):
            if nums[i] not in unique_nums:
                unique_nums.add(nums[i])
                i += 1
            else:
                nums.pop(i)
        return


solution = Solution()

# Example 1
nums1 = [1, 1, 2]
result1 = solution.removeDuplicates(nums1)
print(f"Example 1 - Input: {nums1}, Output: {result1}, nums = {nums1}")

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = solution.removeDuplicates(nums2)
print(f"Example 2 - Input: {nums2}, Output: {result2}, nums = {nums2}")
