# https://leetcode-cn.com/problems/delete-and-earn/
# 740. 删除并获得点数

class Solution:
    def deleteAndEarn(self, nums: list[int]) -> int:
        nums.sort()
        l = len(nums)
        sum1 = 0
        sum2 = 0
        i = 0
        while l:
            curr = nums[i]
            sum1 += curr
            if i + 1 <= l:
                next = curr + 1
                if nums[i+1] == next:
                    sum2 += nums[i+1]
                    l -= 1
                    i += 1
            i += 1
            l -= 1

        return max(sum1, sum2)


nums = [2, 2, 3, 3, 3, 4]
print(Solution().deleteAndEarn(nums))