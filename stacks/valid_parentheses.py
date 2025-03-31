"""
Validate Parentheses
You are given a string s consisting of the following characters: '(', ')', '{', '}', '[' and ']'.

The input string s is valid if and only if:

Every open bracket is closed by the same type of close bracket.
Open brackets are closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Return true if s is a valid string, and false otherwise.
"""


class Solution:
    def is_valid(self, string: str) -> bool:
        brackets_map = {")": "(", "]": "[", "}": "{"}
        stack: list[str] = []
        for char in string:
            if char not in brackets_map:
                stack.append(char)
                continue
            if not stack or stack[-1] != brackets_map[char]:
                return False
            _ = stack.pop()
        return not stack


solution = Solution()

# Example 1
s1 = "[]"
print(
    f"Example 1 - Input: {s1}, Output: {solution.is_valid(s1)}"
)  # Expected Output: True

# Example 2
s2 = "([{}])"
print(
    f"Example 2 - Input: {s2}, Output: {solution.is_valid(s2)}"
)  # Expected Output: True

# Example 3
s3 = "[(])"
print(
    f"Example 3 - Input: {s3}, Output: {solution.is_valid(s3)}"
)  # Expected Output: False
