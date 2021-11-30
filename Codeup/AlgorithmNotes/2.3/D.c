// 问题 D: 习题4-4 三个整数求最大值
// http://codeup.hustoj.com/problem.php?cid=100000567&pid=3

#include <stdio.h>

int main () {
    int a, b, c;
    scanf("%d %d %d", &a, &b, &c);

    int temp;

    if (a < b) {
        
        temp = a;
        a = b;
        b =temp;
    }
    
    if (a < c) {
        temp = a;
        a = c;
        c = temp;
    }

    printf("%d", a);   
}