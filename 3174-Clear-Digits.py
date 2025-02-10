class Solution(object):
    def clearDigits(self, s):
        stack = []
        for i in s:
            if i.isdigit():  
                if stack:
                    stack.pop()
            else:
                stack.append(i)
        return "".join(stack) 
        