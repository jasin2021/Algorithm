# 70. 爬楼梯
# https://leetcode-cn.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2 :
            return n
        a, b, c = 1, 1, 2
        while n:
            a = b
            b = c
            c = a + b
            n -= 1
        return a

s = Solution()
print(s.climbStairs(44))

