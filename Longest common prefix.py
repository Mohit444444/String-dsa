# Given array of strings is [“geeksforgeeks”, “geeks”, “geek”, “geezer”].
# After sorting it becomes [“geek” ,”geeks” ,”geeksforgeeks” ,”geezer”].
# Now, to find the longest common prefix, we only need to compare the first and 
# last strings (“geek” and “geezer“) because any common prefix between these two 
# will also be a prefix for all the strings in between.
# In this case, the common prefix between “geek” and “geezer” is “gee“, 
# which is the longest common prefix for all the strings.

# Input: arr[] = [“geeksforgeeks”, “geeks”, “geek”, “geezer”]
# Output: “gee”
# Explanation: “gee” is the longest common prefix in all the given strings: “geeksforgeeks”, “geeks”, “geeks” and “geezer”.

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs.sort()

        first = strs[0]
        last = strs[-1]
        minLength = min(len(first), len(last))

        i = 0
        while i < minLength and first[i] == last[i]:
            i += 1

        return first[:i]

        # time O(n)
        # spcae O(1)

