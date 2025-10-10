H,W = map(int,input().split())
grid = []
MOD = (10 ** 9 + 7)


for _ in range(H):
    grid.append(input())


dp = [[0] * W for _ in range(H)]
dp[0][0] = 1
for i in range(1,W):
    if grid[0][i] == '.':
        dp[0][i] = dp[0][i - 1]

for i in range(1,H):
    if grid[i][0] == '.':
        dp[i][0] = dp[i - 1][0]


for i in range(1,H):
    for j in range(1,W):
        if grid[i][j] == '.':
            dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

print(dp[H - 1][W - 1] % MOD) 