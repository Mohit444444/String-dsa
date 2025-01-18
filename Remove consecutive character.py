# Input: s = "aabb"
# Output:  "ab" 
# Explanation: 
# The character 'a' at index 2 is the same as 'a' at index 1, so it is removed.
# Similarly, the character 'b' at index 4 is the same as 'b' at index 3, so it is removed.
# The final string is "ab".


class Solution:
    def removeConsecutiveCharacter(self, s):
        i=0
        j=0
        new_elements=''
        
        while(j<len(s)):
            if( s[i]==s[j] ):
                j+=1
             
   
            elif((s[j]!=s[i]) or (j==len(s)-1)):
                new_elements+=s[i]
                i=j
                j+=1
        new_elements+=s[j-1]
        return new_elements
        
        # time O(n)
        # space O(1)