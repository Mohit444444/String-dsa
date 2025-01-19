# Input: S = “geeksforgeeks”
# Output:
# e, count = 4
# g, count = 2
# k, count = 2
# s, count = 2

class Solution:
    def firstRep(self, s):
        count = {}
        
        for i in range(len(s)):
            if(s[i] in count):
                count[s[i]] += 1
            else:
                count[s[i]] = 1
        
        for it,it2 in count.items():  
            if (it2 > 1):   
                print(s(it) + ", count = "+s(it2))


# time O(n)
# space O(1)