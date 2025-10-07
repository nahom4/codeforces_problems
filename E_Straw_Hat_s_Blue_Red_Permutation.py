def rearrange_tresure_chest(zp):
       
        for i in range(n):
            #expected i + 1
            char, value = zp[i]
            if char == 'B' and value < i + 1:
                return False
            
            if char == 'R' and value > i + 1:
                 return False
            
        return True



t = int(input())
for _ in range(t):
    n = int(input())
    array = list(map(int,input().split()))
    letters = list(input())
    zp = list(zip(letters,array))
    zp.sort()
    if rearrange_tresure_chest(zp):
         print("YES")
    else:
         print('NO')



