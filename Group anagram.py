# Example 1:

# Input: strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

# Explanation:

# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.
# Example 2:

# Input: strs = [""]

# Output: [[""]]

# Example 3:

# Input: strs = ["a"]

# Output: [["a"]]

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []
        mp = {}
    
        for i in range(len(strs)):
            s = strs[i]
            s = ''.join(sorted(s))
        
            if s not in mp:
                mp[s] = len(res)
                res.append([])
        
            res[mp[s]].append(strs[i])
    
        return res


        # time O(n * k * log(k))
        # space O(n * k)