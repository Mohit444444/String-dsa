# Input: s = "abba"
# Output: true
# Explanation: "abba" reads the same forwards and backwards, so it is a palindrome.
# Input: s = "abc" 
# Output: false
# Explanation: "abc" does not read the same forwards and backwards, so it is not a palindrome.
# Input: s = "a"
# Output: true
# Explanation: A single-character string is always a palindrome.

class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1
        
        while l < r:
            if s[l] != s[r]:
                return False
            else:
                l += 1
                r -= 1
        
        return s[l] == s[r]