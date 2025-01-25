# Input: s = "abcd"
# Output: 4
# Explanation: palindromic subsequence are : 'a' ,'b', 'c' ,'d'
# Input: s = "aab"
# Output: 4
# Explanation: palindromic subsequence are : 'a', 'a', 'b', 'aa'
# Input: s = "b"
# Output: 1
# Explanation: palindromic subsequence are : 'b'

class Solution:
    def countPS(self,s):
        n = len(s)
        dp = [[0] * n for _ in range(n)]

        # Every single character is a palindrome
        for i in range(n):
            dp[i][i] = 1

        # Fill the table for substrings of length greater than 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] + 1
                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j - 1] - dp[i + 1][j - 1]

        return dp[0][n - 1]
        
        # time O(n^2)
        # space O(n^2)