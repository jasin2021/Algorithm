// 问题 B: 例题5-1-2 连续自然数求和
// http://codeup.hustoj.com/problem.php?cid=100000568&pid=1

#include <stdio.h>

int main() {
    int sum = 0;
    int n = 1;
    
    do {
        sum += n;
        n++;
    } 
    while(n <= 100);

    printf("%d\n",sum);
}