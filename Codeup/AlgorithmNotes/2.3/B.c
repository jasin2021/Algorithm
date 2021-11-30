// 问题 B: 例题4-2 比较交换实数值
// http://codeup.hustoj.com/problem.php?cid=100000567&pid=1

#include <stdio.h>

int main () {
    double a, b;
    scanf("%lf %lf", &a, &b);

    if (a > b) {
        printf("%.2lf %.2lf", b, a);
    }
    
    else {
        printf("%.2lf %.2lf", a, b);
    }   
}