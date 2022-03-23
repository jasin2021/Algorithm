# 剑指 Offer 58 - II. 左旋转字符串
# https://leetcode-cn.com/problems/zuo-xuan-zhuan-zi-fu-chuan-lcof/

class Solution:
    def reverseLeftWords(self, s: str, n: int) -> str:
        l = list(s)
        for i in range(n):
            c = l.pop(0)
            l.append(c)
        return ''.join(l)

s = Solution()
str = 'abcdefg'
k = 2
print(s.reverseLeftWords(str, 2))