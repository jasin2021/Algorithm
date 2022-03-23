class Solution:
    def countHighestScoreNodes(self, parents: list[int]) -> int:
        n = len(list)
        children = [[]] * n
        for i, index in enumerate(parents):
            if i != -1:
                children[i].append(index)

        maxScore, cnt = 0, 0

        def dfs(node: int) -> int:
            score = 1
            size = n - 1
            for ch in children[node]:
                sz = dfs(ch)
                score *= sz
                size -= sz
            if node != 0:
                score *= size
            nonlocal maxScore, cnt
            if score == maxScore:
                cnt += 1
            elif score > maxScore:
                maxScore, cnt = score, 1
            return n - size

        dfs(0)
        return cnt