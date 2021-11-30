# 剑指 Offer 09. 用两个栈实现队列
# https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/

class CQueue:

    def __init__(self):
        self.values = []

    def appendTail(self, value: int) -> None:
        self.values.append(value)
        return self.values

    def deleteHead(self) -> int:
        if self.values == []:
            return -1
        else:
            return self.values.pop(0)
