// 问题 C: 例题4-3 比较交换3个实数值，并按序输出
// http://codeup.hustoj.com/problem.php?cid=100000567&pid=2

#include <stdio.h>

int main () {
    double a, b, c;
    scanf("%lf %lf %lf", &a, &b, &c);

    double temp;

    if (a > b) {
        
        temp = a;
        a = b;
        b =temp;
    }
    
    if (a > c) {
        temp = a;
        a = c;
        c = temp;
    }

    if (b > c) {
        temp = b;
        b = c;
        c =temp;
    }

    printf("%.2lf %.2lf %.2lf", a, b, c);   
}