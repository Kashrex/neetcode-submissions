class MyQueue:

    def __init__(self):
        self.nm=[]
        self.stack2=[]

    def push(self, x: int) -> None:
        self.nm.append(x)

    def pop(self) -> int:
        while len(self.nm) > 1:
            self.stack2.append(self.nm.pop())
        res = self.nm.pop()
        while self.stack2:
            self.nm.append(self.stack2.pop())
        return res



    def peek(self) -> int:
        return self.nm[0]

    def empty(self) -> bool:
        return len(self.nm)==0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()