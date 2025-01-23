# Example 1:

# Input: s = "ABAB", k = 2
# Output: 4
# Explanation: Replace the two 'A's with two 'B's or vice versa.
# Example 2:

# Input: s = "AABABBA", k = 1
# Output: 4
# Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
# The substring "BBBB" has the longest repeating letters, which is 4.
# There may exists other ways to achieve this answer too.

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)
        freq = {}
        maxFreq = 0
        res = 0
        l = 0

        for r in range(n):
            freq[s[r]] = freq.get(s[r], 0) + 1
            maxFreq = max(maxFreq, freq[s[r]])

            if r - l + 1 - maxFreq > k:
                freq[s[l]] -= 1
                l += 1

      
            res = max(res, r - l + 1)

        return res

# Time Complexity: O(n)
# Space Complexity: O(1)