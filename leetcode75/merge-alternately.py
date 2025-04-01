"""
You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
Return the merged string.

Constraints:
1 <= word1.length, word2.length <= 100
word1 and word2 consist of lowercase English letters.
"""


def mergeAlternately(word1: str, word2: str) -> str:
    result: list[str] = []
    m, n = len(word1), len(word2)
    i, j = 0, 0
    while i < m or j < n:
        if i < m:
            result.append(word1[i])
            i += 1
        if j < n:
            result.append(word2[j])
            j += 1
    return "".join(result)


# Test cases
print(mergeAlternately("abc", "pqr"))  # Output: "apbqcr"
print(mergeAlternately("ab", "pqrs"))  # Output: "apbqrs"
print(mergeAlternately("abcd", "pq"))  # Output: "apbqcd"
