# Example 1:

# Input: s = "babad"
# Output: "bab"
# Explanation: "aba" is also a valid answer.
# Example 2:

# Input: s = "cbbd"
# Output: "bb"

class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        if n == 0:
            return ""

        start = 0
        max_len = 1

        for i in range(n):
            for j in range(2):
                low = i
                hi = i + j

           
                while low >= 0 and hi < n and s[low] == s[hi]:
                    curr_len = hi - low + 1
                    if curr_len > max_len:
                        start = low
                        max_len = curr_len
                    low -= 1
                    hi += 1

        return s[start:start + max_len]

        # time O(n^2)
        # space O(1)