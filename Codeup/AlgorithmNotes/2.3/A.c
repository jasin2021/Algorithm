// 问题 A: 例题4-1 一元二次方程求根
// http://codeup.hustoj.com/problem.php?cid=100000567&pid=0

#include <stdio.h>

int main () {
    double a, b, c;
    double r1, r2;
    double delta;

    scanf("%lf %lf %lf", &a, &b, &c);
    
    delta = b * b - 4 * a * c;
    if (delta < 0) {
        printf("No real roots!\n");
    }

    else {
        delta = sqrt(delta);
        r1 = (-b + pow(delta, 0.5)) / 2 / a;
        r2 = (-b - pow(delta, 0.5)) / 2 / a;
        printf("r1=%7.2lf\n", r1);
        printf("r2=%7.2lf", r2);
    }

    return 0;
}