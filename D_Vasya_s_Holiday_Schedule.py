n = int(input())
days = list(map(int, input().split()))

INF = float("inf")
dp = [[INF] * 3 for _ in range(n + 1)]

dp[0][0] = 0  

for i in range(1, n + 1): # 1 3 2 0
    activity = days[i - 1]

    dp[i][0] = min(dp[i - 1]) + 1 # rest

    if activity in (1, 3): # coding
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2])

    if activity in (2, 3): #sporting
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1])

print(dp)
print(min(dp[n]))
