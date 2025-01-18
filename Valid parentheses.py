# Example 1:
# Input: s = "()"
# Output: true

# Example 2:
# Input: s = "()[]{}"
# Output: true

# Example 3:
# Input: s = "(]"
# Output: false

# Example 4:
# Input: s = "([])"
# Output: true

class Solution:
    def isValid(self, s: str) -> bool:
        st = []

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                st.append(s[i])
        
            else:
                if st and ((st[-1] == '(' and s[i] == ')') or 
                    (st[-1] == '{' and s[i] == '}') or
                    (st[-1] == '[' and s[i] == ']')):
                    st.pop()
                else:
                    return False

        return not st


        # time O(n)
        # space O(n)