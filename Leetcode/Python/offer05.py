# 剑指 Offer 05. 替换空格
# https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/

class Solution:
    def replaceSpace(self, s: str) -> str:
        l = list(s)
        lenth = len(l)
        for i in range(lenth):
            if l[i] == ' ':
                l[i] = '%20'
        return ''.join(l)



s = Solution()
str = "We are happy."
print(s.replaceSpace(str))