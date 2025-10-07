def solve():
   
    n, k = map(int, input().split())
    h = list(map(int, input().split()))
    p = list(map(int, input().split()))

    monsters = sorted(zip(p, h))

    a = k
    i = 0

    while k > 0 and i < n:
        while i < n and monsters[i][1] <= a:
            i += 1

        if i < n:
            k -= monsters[i][0] 

        a += k

    if i >= n:
        print('YES')
    
    else:
        print('NO')
    

t = int(input())
for _ in range(t):
    solve()