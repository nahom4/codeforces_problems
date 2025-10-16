import sys
sys.setrecursionlimit(10**6)

n, k = map(int, input().split())
A = list(map(int, input().split()))

mn = min(A)
# the question is does first win?
dp = [[None] * (k + 1) for _ in range(2)]
# print(dp)

zero = 0
one = 1

for i in range(mn):
    dp[zero][i] = False
    dp[one][i] = True

for i in range(mn,k + 1):      
    any = False
    all = True
    for j in range(n):
        if A[j] > i:
            continue
        any |= dp[one][i - A[j]]
        all &= dp[zero][i - A[j]]
    
    dp[zero][i] = any
    dp[one][i] = all

# print(dp)

if dp[zero][k]:
    print('First')
else:
    print('Second')


# #lets get it done the issue is with the base case so full fill it
# dp = [[None] * (k + 1) for _ in range(2)]

# def memoized_solution(player,k):
#     if k < mn: #base case
#         if player == 0: 
#             return False
#         if player == 1:
#             return True 
     
#     if dp[player][k] is not None:
#         return dp[player][k] 
    
#     ans = []
#     for i in range(n):
#         ans.append(memoized_solution(1 - player,k - A[i]))

#     if player == 0:
#         dp[player][k] = any(ans)
    
#     if player == 1:
#         dp[player][k] = all(ans)

#     return dp[player][k]
    
# # print(dp)

# if memoized_solution(0,k):
#     print('First')
# else:
#     print('Second')
