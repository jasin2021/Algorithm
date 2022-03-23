// 问题 A: 例题5-1-1 连续自然数求和
// http://codeup.hustoj.com/problem.php?cid=100000568&pid=0

#include <stdio.h>

int main () {
    int n = 100;
    int sum = 0;
    int i;
    for (i = 1; i <= n; i++) {
        sum += i;
    }
    printf("%d\n", sum);
}