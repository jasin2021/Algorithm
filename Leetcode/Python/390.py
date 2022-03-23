class Solution:
    def lastRemaining(self, n: int) -> int:
        c = 1
        a = 1
        b = n
        l = n
        while a != b:
            if l % 2 == 0:
                a += c
                l /= 2
                c *= 2
            else:
                a += c
                b -= c
                l = int(l/2)
                c *= 2
            if l > 1:
                if l % 2 == 0:
                    b -= c
                    l /= 2
                    c *= 2
                else:
                    a += c
                    b -= c
                    l = int(l/2)
                    c *= 2
        return a

n = 9
print(Solution().lastRemaining(n))