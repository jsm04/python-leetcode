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
    def isValid(self, string: str) -> bool:
        characters_map = {")": "(", "]": "[", "}": "{"}
        stack = []

        for char in string:
            if char not in characters_map:
                stack.append(char)
                continue
            if not stack or stack[-1] != characters_map[char]:
                return False
            stack.pop()

        return not stack


"""
Example 1:
Input: s = "[]"
Output: true

Example 2:
Input: s = "([{}])"
Output: true

Example 3:
Input: s = "[(])"
Output: false

Explanation: The brackets are not closed in the correct order.
Constraints:
1 <= s.length <= 1000
"""
