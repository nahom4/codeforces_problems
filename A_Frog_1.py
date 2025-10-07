n = int(input())
stones = list(map(int,input().split()))

dp = [0] * n
dp[1] = abs(stones[0] - stones[1])

for i in range(2,n):
    first_jump = abs(stones[i] - stones[i - 1])
    second_jump = abs(stones[i] - stones[i - 2])
    dp[i] = min(dp[i - 1] + first_jump ,dp[i - 2] + second_jump)

print(dp[-1])