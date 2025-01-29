from collections import deque
class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = deque()
        stack.append("$")
        for i in range(0,len(s)):
            if s[i] == stack[-1]:
                stack.pop()
            else:
                stack.append(s[i])
        stack.popleft()
        return "".join(stack)