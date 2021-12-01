# 剑指 Offer 30. 包含min函数的栈
# https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.values = []

    def push(self, x: int) -> None:
        self.values.append(x)

    def pop(self) -> None:
        self.values.pop()

    def top(self) -> int:
       return self.values[-1] 

    def min(self) -> int:
        return min(self.values)



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.min()