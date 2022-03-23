// 问题 E: 习题4-10-1 奖金计算
// http://codeup.hustoj.com/problem.php?cid=100000567&pid=4

#include <cstdio>

int main(){
    double sales, profit;
    scanf("%lf", &sales);
    if(sales <= 100000)
        profit = sales * 0.1;
    else if(sales > 100000 && sales <= 200000)
        profit = (sales - 100000) * 0.075 + 100000 * 0.1;
    else if(sales > 200000 && sales <= 400000)
        profit = (sales - 200000) * 0.05 + 100000 * 0.1 + 100000 * 0.075;
    else if(sales > 400000 && sales <= 600000)
        profit = (sales - 400000) * 0.03 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05;
    else if(sales > 600000 && sales <= 1000000)
        profit = (sales - 600000) * 0.015 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03;
    else if(sales > 1000000)
        profit = (sales - 1000000) * 0.01 + 100000 * 0.1 + 100000 * 0.075 + 200000 * 0.05 + 200000 * 0.03 + 400000 * 0.015;
    printf("%.2f\n", profit);
    return 0;
}
	