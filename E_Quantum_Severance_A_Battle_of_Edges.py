def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))

        positive_sum = 0
        ans = 0

        for i in range(n):
            if a[i] < 0 :
                ans = max(ans - a[i],positive_sum - a[i])
            else:
                positive_sum += a[i]

        print(max(positive_sum,ans))
                
solve()
