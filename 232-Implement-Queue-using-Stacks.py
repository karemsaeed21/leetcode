class MyQueue:

    def __init__(self):
        self.stack = deque()
        self.stack1 = deque()

    def push(self, x: int):
        self.stack.append(x)

    def pop(self) -> int:
        while len(self.stack)>1:
            self.stack1.appendleft(self.stack.pop())
        element = self.stack.pop()
        
        while self.stack1:
            self.stack.append(self.stack1.popleft())

        return element
    def peek(self) -> int:
        while self.stack:
            self.stack1.appendleft(self.stack.pop())
        element = self.stack1[0]
        
        while self.stack1:
            self.stack.append(self.stack1.popleft())
        
        return element

    def empty(self) -> bool:
        return 0 if self.stack else 1


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()