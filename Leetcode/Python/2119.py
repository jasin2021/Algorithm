class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        a = str(num)[::-1]
        a = int(a)
        a = str(a)[::-1]
        a = int(a)
        if a == num:
            return True
        return False


num = 1800
print(Solution().isSameAfterReversals(num))
