class Solution:
    def platesBetweenCandles(self, s: str, queries: list[list[int]]) -> list[int]:
        n = len(s)
        prefix = [0] * n
        left = [0] * n
        right = [0] * n
        pos = 0
        for i in range(n):
            if s[i] == '|':
                pos = i
                break
        flag = pos
        for i in range(flag + 1, n):
            if s[i] == '|':
                prefix[i] = prefix[i - 1] + i - pos -1
                pos = i
            else:
                prefix[i] = prefix[i - 1]
            left[i] = pos

        pos = n - 1
        for i in range(n - 1, -1, -1):
            if s[i] == '|':
                pos = i
            right[i] = pos



        re = []
        for li in queries:
            temp = prefix[left[li[1]]] - prefix[right[li[0]]]
            if temp < 0:
                temp = 0
            re.append(temp)


        return re


s = "***"
qureies = [[2, 2]]
print(Solution().platesBetweenCandles(s, qureies))

