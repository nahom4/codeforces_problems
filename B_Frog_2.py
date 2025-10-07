n,k = map(int,input().split())
nums = list(map(int,input().split()))

dp = [float("inf")] * n
dp[0] = 0

for i in range(n):
    for j in range(max(0, i - k), i): #j -> j - k, max 0
        dp[i] = min(dp[i], dp[j] + abs(nums[i] - nums[j]) )

print(dp[n - 1])