n = int(input())
nums = list(map(float,input().split()))

dp = [[0] * (n + 1) for _ in range(n + 1)]

dp[n - 1][1] = nums[n - 1] 
dp[n - 1][0] = 1 - nums[n - 1]

for i in range(n - 2,-1,-1):
    for j in range(n, -1, -1):
        dp[i][j] = nums[i] * dp[i + 1][j - 1] + (1 - nums[i]) * dp[i + 1][j]

ans = 0
for i in range(n, -1,-1):  # 2
    
    if i <= (n - i):
        break
    res = dp[0][i]
    ans += res
    # print(res)

print(ans)

# def memoize(i, k):
#     if i >= n:
#         if k == 0:
#             return 1
#         return 0
#     if dp[i][k] > 0:
#         return dp[i][k]

#     dp[i][k] = nums[i] * memoize(i + 1, k - 1) + (1 - nums[i] ) * memoize(i + 1, k)
#     return dp[i][k]


# ans = 0
# for i in range(n, -1,-1):  # 2
    
#     if i <= (n - i):
#         break
#     res = memoize(0,i)
#     ans += res
#     # print(res)

# print(ans)
