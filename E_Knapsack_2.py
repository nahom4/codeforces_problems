n,w  = map(int,input().split())

store = []

max_ans = 1
for _ in range(n):
    store.append(tuple(map(int,input().split())))
    max_ans += store[-1][1]

dp = [[float("inf")] * (max_ans + 1) for _ in range(n) ]

'''
let's convert the top down code into bottom up
we just have to update to figure out the update pattern
we will be keeping track of the weight right min weight for a given (i,k)
(n - 1, ) offcourse I will only be able to update only my own value

'''
for i in range(max_ans + 1):
    if i == store[-1][1]:
        dp[-1][i] = store[-1][0] 

for i in range(n):
    dp[i][0] = 0
    
# base case 
for i in range(n - 2, -1,-1):
    for j in range(max_ans):
        obj_w, obj_v = store[i]
        dp[i][j] = min(dp[i + 1][j], obj_w + dp[i + 1][j - obj_v])

for k in range(max_ans,-1,-1):
    total = dp[0][k]
    if total <= w:
        break

print(k)
# def dp(i, k):
    
#     if i >= n:
#         if k == 0 :
#             return 0
        
#         return float('inf')
    

#     if cache[i][k] != float("inf"):
#         return cache[i][k]
    
#     if k < 0:
#         return float('inf') # bad move right
    
#     obj_w, obj_v = store[i]
#     cache[i][k] = min(dp(i + 1, k), obj_w + dp(i + 1, k - obj_v ))

#     return cache[i][k]


# for k in range(max_ans,-1,-1):
#     total = dp(0,k)
#     if total <= w:
#         break

# print(k)
