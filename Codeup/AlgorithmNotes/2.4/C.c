// 问题 C: 例题5-1-3 连续自然数求和
// http://codeup.hustoj.com/problem.php?cid=100000568&pid=2

int main () {
    int n = 100;
    int sum = 0;
    int i;
    for (i = 1; i <= n; i++) {
        sum += i;
    }
    printf("%d\n", sum);
}