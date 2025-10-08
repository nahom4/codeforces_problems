n,w = map(int,input().split()) 

store = []
for _ in range(n):
    store.append(tuple(map(int,input().split())))


dp = [[0] * (w + 1) for _ in range(n + 1)]
# start from the base case

for i in range(n - 1,-1,-1):
    for w in range(w + 1):
        obj_w,obj_v = store[i]
        if obj_w <= w:
            dp[i][w] = max(dp[i + 1][w - obj_w] + obj_v, dp[i + 1][w])
        else:
            dp[i][w] = dp[i + 1][w]

print(dp[0][w])
# def dp(i,w):
#     if w < 0:
#         return float("-inf")
#     if i >= n:
#         return 0
    
#     if cache[i][w] != float("inf"):
#         return cache[i][w]
    
#     cache[i][w] = max(dp(i + 1, w), (store[i][1] + dp(i + 1, w - store[i][0])))
#     return cache[i][w]

# print(dp(0,w))