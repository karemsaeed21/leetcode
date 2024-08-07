class Solution:
    def maxDepth(self, s):
        current_depth = 0
        max_depth = 0
        for x in s:
            if x == "(":
                current_depth +=1
                max_depth = max(current_depth,max_depth)
            elif x == ")":
                current_depth -=1
        return max_depth 