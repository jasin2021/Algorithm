# https://leetcode-cn.com/problems/two-sum/
# 1. 两数之和

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dct = {}
        for i, n in enumerate(nums):
            cp = target - n
            if cp in dct:
                return [dct[cp], i]
            else:
                dct[n] = i