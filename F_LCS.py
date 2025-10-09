x = input()
y = input()

m,n = len(x),len(y)
dp = [[0] * (m + 1) for _ in range(n + 1)]

for i in range(n - 1,-1,-1):
    for j in range(m - 1,-1,-1):
        if x[j] == y[i]: # we are good right
            dp[i][j] = 1 + dp[i + 1][j + 1]
        else:
            dp[i][j] = max(dp[i][j + 1],dp[i + 1][j], dp[i + 1][j + 1])

i,j = 0,0
# m,n = len(x),len(y)

ans = []
while i < n and j < m:
    if x[j] == y[i]:
        ans.append(x[j])
        i += 1
        j += 1
    
    else:
        (i,j) = max((i + 1,j + 1),(i, j + 1),(i + 1,j), key=lambda x : dp[x[0]][x[1]])

print(''.join(ans))


# def dp(i,j):
#     if i >= m:
#         return ''
    
#     if j >= n:
#         return ''
    

#     if x[i] == y[j]: # we are good right

#         return x[i] + dp(i + 1, j + 1)
    
#     x_str = dp(i, j + 1)
#     y_str = dp(i + 1, j + 1)
#     z_str = dp(i + 1, j)

#     return max(x_str,y_str,z_str, key=lambda x : len(x))


# print(dp(0,0))