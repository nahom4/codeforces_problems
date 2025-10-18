n = int(input())

queue = list(map(int,input().split()))

dp = [[(0,0) for _ in range(n + 1)] for _ in range(n + 1)]

'''
The direction of filling is going to be difficult offcourse

state (0 , n - 1)  damn the direction is a decreasing j - i 
the width is what should guide the way fill it 

'''

for i in range(n - 1, -1,-1):
    for j in range(n): #expand
        if i > j: 
            continue

        X_L, Y_L = dp[i + 1][j]
        X_R, Y_R = dp[i][j - 1]

        if (n - (i + j)) % 2 : #X's turn
            dp[i][j] = max((X_L + queue[i], Y_L), (X_R + queue[j], Y_R))
        else:
            dp[i][j] = max((X_L, Y_L + queue[i]), (X_R,Y_R + queue[j]), key=lambda x : x[1])


X,Y = dp[0][n - 1]

print(X - Y)

# def dp(i,j): # x + y even is firsts move odd is second to move

#     if i > j:
#         return (0,0) # X, Y
    
#     X_L, Y_L = dp(i + 1, j)  
#     X_R, Y_R = dp(i, j - 1)

#     if (n - (i + j)) % 2 : #X's turn
#         # print('first')
#         return max((X_L + queue[i], Y_L), (X_R + queue[j], Y_R))
#     # print('second')
#     return max((X_L, Y_L + queue[i]), (X_R,Y_R + queue[j]), key=lambda x : x[1])


# X,Y = dp(0, n - 1)

# print(X - Y)



