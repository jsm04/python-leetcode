"""
Given an integer array nums, return the greatest common divisor of the smallest number and largest number in nums.
The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.
"""


class Solution:
    def findGCD(self, nums: list[int]) -> int:
        # Implement your solution here
        pass


# Test cases - Example 1:
nums = [2, 5, 6, 9, 10]
# Expected output: 2
print(Solution().findGCD(nums))

# Example 2:
nums = [7, 5, 6, 8, 3]
# Expected output: 1
print(Solution().findGCD(nums))

# Example 3:
nums = [3, 3]
# Expected output: 3
print(Solution().findGCD(nums))
