# https://leetcode-cn.com/problems/fibonacci-number/
# 509. 斐波那契数

class Solution:
    def fib(self, n: int) -> int:
        if n == 0 or n == 1:
            return n 
        a, b, c = 0, 1, 1
        while n:
            a = b
            b = c
            c = a + b
            n -= 1
        return a

s = Solution()
print(s.fib(4))