# 剑指 Offer 10- I. 斐波那契数列
# https://leetcode-cn.com/problems/fei-bo-na-qi-shu-lie-lcof/

class Solution:
    def fib(self, n: int) -> int:
        MOD = 10 ** 9 + 7
        if n == 0 or n == 1:
            return n
        a, b, c = 0, 1, 1 
        while n:
            a = b
            b = c
            c = a + b
            n -= 1
        return a % MOD
            
s = Solution()
print(s.fib(3))
