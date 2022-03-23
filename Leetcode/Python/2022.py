class Solution:
    def construct2DArray(self, original: list[int], m: int, n: int) -> list[list[int]]:
        re = []
        l = len(original)
        if m*n != l:
            return re

        k = 0
        for i in range(m):
            a = []
            for j in range(n):
                a.append(original[k])
                k += 1
            re.append(a)
        return re


original = [1, 2, 3, 4]
m = 1
n = 3

print(Solution().construct2DArray(original, m, n))