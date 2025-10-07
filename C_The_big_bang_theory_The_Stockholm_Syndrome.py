def solve():
    n = int(input())
    array = list(map(int,input().split()))
    ans = 0
    array.sort()

    for i in range(n): # 2
        if array[i] > ans:
            ans += 1
    
    print(ans + 1)


solve()