// 问题 E: 例题3-5 求一元二次方程的根
// http://codeup.hustoj.com/problem.php?cid=100000566&pid=4


#include <stdio.h>
#include <math.h>

int main () {
    double a, b, c;
    double r1, r2;
    double delta;
    scanf("%lf %lf %lf", &a, &b, &c);
    delta = sqrt(b * b - 4 * a * c);
    r1 = (-b + pow(delta, 0.5)) / 2 / a;
    r2 = (-b - pow(delta, 0.5)) / 2 / a;
    printf("r1=%7.2lf\n", r1);
    printf("r2=%7.2lf", r2);
    return 0;
}