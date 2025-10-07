def solve():
    n,k,q = map(int,input().split())
    array = list(map(int,input().split()))

    ct = 0
    left = 0
    ans = 0

    for right in range(n):
        if array[right] > q:
            left = right + 1
            ct = 0

        if right - left + 1 >= k:
            ct += 1

        ans += ct 
    
    return ans


t = int(input())
for _ in range(t):
    print(solve())
