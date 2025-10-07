from collections import Counter
import math
def solve():
    t = int(input())
    for _ in range(t):
        n,k = map(int,input().split())
        array = list(map(int,input().split()))
        array = list(map(lambda x : x % k, array))
        ct = Counter(array)
        mx = 0
        # print(ct)
        for key,count in ct.items(): # {8: 3, 7: 2, 1: 1, 3: 1, 5: 1, 10: 1, 9: 1} x = 

                                    # 6 12  18 24 
            div = math.ceil(key / k)
            if key % k:
                curr =  div * k + (count - 1 ) * k - key + 1
                mx = max(mx,curr)
             
        print(mx) 

solve()