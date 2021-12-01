# https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/
# 3. 无重复字符的最长子串

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = len(s)
        lenth = 0
        str = ""
        index = 0
        li = [0, 0]
        i = 0
        while i < l:
            flag = 1
            for j in range(lenth):
                if str[j] == s[i]:
                    i = j + index + 1
                    flag = 0
                    index = i
                    str = ''
                    lenth = 0
                    break
            if flag:
                lenth += 1
                str += s[i]
                if lenth > li[1]:
                    li = [index, lenth]
                i += 1
            
        return li[1]

s = Solution()

print(s.lengthOfLongestSubstring("bedasac"))
