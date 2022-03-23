# https://leetcode-cn.com/problems/min-cost-climbing-stairs/
# 746. 使用最小花费爬楼梯

class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        n = len(cost)
        prev, curr = 0, 0
        for i in range(2, n + 1):
            next = min(prev + cost[i-2], curr + cost[i-1])
            prev, curr = curr, next
        return next


s = Solution()
print(s.minCostClimbingStairs([10,15,20]))
                
            
