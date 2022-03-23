# 198. 打家劫舍
# https://leetcode-cn.com/problems/house-robber/


class Solution:
    def rob(self, nums: list[int]) -> int:
        l = len(nums)
        if l == 1:
            return nums[0]
        prev = 0
        curr = 0
        for i in range(l):
            next = nums[i]
            temp = prev + next
            if temp > curr:
                prev = curr
                curr = temp
            else:
                prev = curr
        return curr


nums = [1, 4, 3, 0]
print(Solution().rob(nums))
