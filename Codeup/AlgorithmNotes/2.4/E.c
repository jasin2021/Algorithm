// http://codeup.hustoj.com/problem.php?cid=100000568&pid=4
// 问题 E: 例题5-1-5 连续自然数求和

#include <stdio.h>

int main () {
    int n = 1000;
    int sum = 0;
    int i = 0;
    while(1) {
        if (sum > n) break;
        i++;
        sum += i;
    }
    printf("%d\n", i);
}