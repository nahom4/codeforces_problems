def solve():
    n = int(input())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    b_map = {b[i] : i for i in range(n)}

    ct = 0
    last = a[0]
    for i in range(1,n):
        if b_map[last] < b_map[a[i]]: # good
            last = a[i]
        else:
            ct += 1

    print(ct)

solve()
            


