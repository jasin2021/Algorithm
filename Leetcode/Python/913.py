class Solution:
    def catMouseGame(self, graph: list[list[int]]) -> int:
        m = 1
        c = 2
        s = {1, 2}
        t = 0
        if 0 in graph[m]:
            return 1
        flag = True
        while True:
            for i in graph[m]:
                if i in s:
                    continue
                m = i
                if m == 0:
                    return 1
                s.add(i)
                for j in graph[c]:
                    if j == 0:
                        continue
                    if j in s:
                        continue
                    if j == m:
                        return 2
                    c = j
                    flag = False
                    s.add(c)
            if flag:
                return 0


graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
print(Solution().catMouseGame(graph))
