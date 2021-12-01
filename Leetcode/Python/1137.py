# https://leetcode-cn.com/problems/n-th-tribonacci-number/
# 1137. 第 N 个泰波那契数

class Solution:
    def tribonacci(self, n: int) -> int:
        if n == 0 or n == 1: 
            return n
        a, b, c, d = 0, 1, 1, 2
        while n:
            a = b
            b = c
            c = d
            d = a + b + c
            n -= 1
        return a

s = Solution()
print(s.tribonacci(25))        
        