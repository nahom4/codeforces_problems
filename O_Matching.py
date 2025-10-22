N = int(input())

grid = [] # we don't need a grid

for _ in range(N):
    grid.append(int(input().replace(" ", ""), 2))

# print(grid)
MOD = (10 ** 9 + 7)
max_num = 2 ** N   # what's wrong here  # n = 2 [1,1,1]  7 is the max bit szie 2 ^ 3 = 8 
dp = [0] * max_num  #base case
dp[max_num - 1] = 1
# we will optimize it later
# so we got to remove one loop i feel like math could be the key
for bit_store in range(max_num - 2,-1,-1): #this is good right
    # for i in range(N):
    # print(bit_store)
    count = 0
    mask = 1
    # this is very ripe for optimization 
    # mask | bit_store is actually generated right
    # 2  8  16 32
    # 23 27 38 38 N - 1 I will be taking some and leaving some right and I want to do it in one go
    i = bit_store.bit_count()  # turned on bits
    # print(i)
    for _ in range(N) : # I could be wrong here
        if (grid[i] & mask) and not(mask & bit_store): #needs to be free in the mask and in the grid
            # print(mask | bit_store,max_num)
            count = (count + dp[mask | bit_store]) % MOD
        mask <<= 1  #left shift

    
    dp[bit_store] = count % MOD#this bad right it will over wright
        
# print(dp) 
print(dp[0] % MOD)

# def recursive(i, bit_store):

#     if i >= N: # we ran out but we shouldn't get here if we didn't pair right
#         return 1 
    
#     if dp[i][bit_store] is not None:
#         return dp[i][bit_store]
#     # print(bit_store)
#     count = 0
#     mask = 1
#     j = 0
#     while j < N: # I could be wrong here
#         if grid[i][j] and not(mask & bit_store): #needs to be free in the mask and in the grid
#             count += recursive(i + 1, mask | bit_store)
#         j += 1
#         mask <<= 1  #left shift

#     dp[i][bit_store] = count
    
#     return dp[i][bit_store]

# print(recursive(0,0))


