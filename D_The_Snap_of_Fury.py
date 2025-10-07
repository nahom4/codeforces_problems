def solve():
    n = int(input())
    a = list(map(int,input().split()))
    prefix_sum = [0] * (n + 1)

    for i in range(n): # 0 1 0 10  #-2 1 0 1
        r = a[i]
        idx = max(i - r,0)
        prefix_sum[idx] -= 1
        prefix_sum[i] += 1

    ct = 0
    for i in range(n):
        prefix_sum[i] += prefix_sum[i - 1]
        if prefix_sum[i] >= 0:
            ct += 1

    print(ct)

solve()




