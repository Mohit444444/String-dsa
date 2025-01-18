# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true

# Example 2:
# Input: s = "rat", t = "car"
# Output: false

from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        dic1 = Counter(s)
        dic2  = Counter(t)

        return dic1 == dic2


        # time O(n)
        # space O(n)
