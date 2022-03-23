class Solution:
    def subArrayRanges(self, nums: list[int]) -> int:
        l = len(nums)
        s = 0
        for i in range(l):
            for j in range(i+1,l):
                s += nums[j] - nums[i] if nums[j] - nums[i] > 0 else nums[i] - nums[j]
        return s


nums = [4, -2, -3, 4, 1]
print(Solution().subArrayRanges(nums))