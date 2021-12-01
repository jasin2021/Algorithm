# 26. 删除有序数组中的重复项
# https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        nus = sorted(list(set(nums)))
        for i in range(len(nus)):
            nums[i] = nus[i]
        return len(nus)