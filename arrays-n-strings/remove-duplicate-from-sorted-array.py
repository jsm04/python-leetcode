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
        if not nums:
            return 0
        next_pointer = 0  # Tracks the last unique element

        for i in range(1, len(nums)):
            if nums[i] != nums[next_pointer]:  # Found a new unique value
                next_pointer += 1
                nums[next_pointer] = nums[i]  # Move it forward
        return next_pointer + 1  # New length of unique elements


s = Solution()

# Example 1
nums1 = [1, 1, 2]
result1 = s.removeDuplicates(nums1)
print(f"Example 1 - Input: {nums1}, Output: {result1}, nums = {nums1}")

# Example 2
nums2 = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
result2 = s.removeDuplicates(nums2)
print(f"Example 2 - Input: {nums2}, Output: {result2}, nums = {nums2}")
