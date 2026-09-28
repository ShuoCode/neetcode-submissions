class MyStack:
    # Two ways to pop correct item from the queue
    # One is to reverse the order when pop()
    # Another one is to reverse the order when push()
    # Current method is the first one
    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        self.q.append(x) 

    def pop(self) -> int:
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft()) 
        return self.q.popleft()

    def top(self) -> int:
        return self.q[-1]
        

    def empty(self) -> bool:
        return len(self.q) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()