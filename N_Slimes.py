n = int(input())
nums = list(map(int,input().split()))

dp = [[(float("inf"),float("inf")) for _ in range(n + 1)] for _ in range(n + 1)]

for i in range(n):
    for j in range(n):
        if i == j:
            dp[i][j] = (0,nums[i]) 

for i in range(1,n): 
    for j in range(n): 
        mn_cost = (float("inf"),0)
        last = min(i + j,n) 
        for k in range(j, last): 
            left_c,left_w = dp[j][k] 
            right_c,right_w = dp[k + 1][last] 
            
            mn_cost = min((left_w + right_w + left_c + right_c, left_w + right_w),mn_cost)
        
        dp[j][last] = mn_cost 

print(dp[0][n - 1][0])
# def recursive(i,j):

#     # print(i,j)
#     # the approach is correct
#     # what I am missing is proly index stuff and min logic
#     # why is the total sum wrong
#     if i == j: # base case this is the issue you can do base case first
#         return (nums[i],0)
    
#     if dp[i][j] != (0,0):
#         return dp[i][j]
    
#     mn_cost = (float("inf"),0) # (1,2,3,4,5)
#     for k in range(i,j):  # the issue is here I am not cosidering the last element right I am tho
#         # The common proeperty is the distance between i and j I should start from small and expand
#         left_w,left_c = recursive(i,k)
#         right_w, right_c = recursive(k + 1,j)
        
#         mn_cost = min((left_w + right_w,left_c + right_c + left_w + right_w),mn_cost) # this will calculate the sum but we are not really after that right

#     # print(i,j,mn_cost)  
#     dp[i][j] = mn_cost
#     return dp[i][j]

# print(recursive(0,n - 1)[1])
