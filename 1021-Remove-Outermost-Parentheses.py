class Solution:
    def removeOuterParentheses(self, s):
        val = 0 
        ans = []
        idx = 0 
        for i in range(len(s)):
            if s[i] == "(":
                val += 1 
            else: 
                val -= 1 
            if val == 0:
                ans.append(s[idx:i+1])
                idx = i + 1
        t = ""
        for par in ans:
            t += par[1:-1]
        return t