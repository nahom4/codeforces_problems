n,k = map(int,input().split())
candies = list(map(int,input().split()))

dp = [[0] * (k + 1) for _ in range(n + 1)]
dp[n][0] = 1 # base case
prefix = [1] * (k + 2)
prefix[k + 1] = 0  #buffer
MOD = (10 ** 9 + 7)

for i in range(n - 1,-1,-1):
    temp = [0] * (k + 2)
    for j in range(k + 1):
        
        diff = prefix[j] - prefix[j - min(candies[i],j) - 1]
        dp[i][j] += diff
        temp[j] +=( temp[j - 1] + dp[i][j]) % MOD
        # for c in range(min(candies[i],k) + 1):
        #     dp[i][j] += dp[i + 1][j - c]

    prefix = temp

# print(dp)
print(dp[0][k] % MOD)

# def recursive (i,k):
    
#     if i >= n:
#         if k == 0:
#             return 1
        
#         return 0
#     if dp[i][k] is not None:
#         return dp[i][k]
    
#     count = 0
#     for j in range(min(candies[i],k) + 1):
#         count += recursive(i + 1, k - j)

#     # print(count)
#     dp[i][k] = count
#     return dp[i][k]

# print(recursive(0,k))