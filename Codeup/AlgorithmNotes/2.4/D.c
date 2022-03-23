// 问题 D: 例题5-1-4 连续自然数求和
// http://codeup.hustoj.com/problem.php?cid=100000568&pid=3

int main () {
    int n;
    scanf("%d", &n);
    int sum = 0;
    int i = 0;
    while (1) {
        if (i > n) break;
        sum += i;
        i++;
    }
    printf("%d\n", sum);
}