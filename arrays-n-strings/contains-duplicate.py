"""
Duplicate Integer
Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.
"""


class Solution:
    def contains_duplicate(self, nums: list[int]) -> bool:
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False


# Instantiate the Solution class
solution = Solution()

# Example 1
nums1 = [1, 2, 3, 3]
print(
    f"Example 1 - Input: {nums1}, Output: {solution.contains_duplicate(nums1)}"
)  # Expected Output: True

# Example 2
nums2 = [1, 2, 3, 4]
print(
    f"Example 2 - Input: {nums2}, Output: {solution.contains_duplicate(nums2)}"
)  # Expected Output: False
