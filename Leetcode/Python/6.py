class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        lis = [''] * numRows
        j = 0
        for i in s:
            k = j % (2*numRows-2)
            j += 1
            if k <= numRows - 1:
                print(lis)
                lis[k] += i
            elif k > numRows-1:
                lis[2*numRows-2-k] += i

        return ''.join(lis)


str = "PAYPALISHIRING"
n = 3
print(Solution().convert(str,n))

