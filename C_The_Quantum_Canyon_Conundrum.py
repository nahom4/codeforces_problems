def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int,input().split()))
        d_a = []
        st = set()
        for i in range(n):
            if  a[i] not in st:
                d_a.append(a[i])
                st = set()
                st.add(a[i])

        d_a.append(float('inf'))

        ct = 0
        for i in range(len(d_a) - 1):
            if d_a[i - 1] > d_a[i] < d_a[i + 1]:
                ct += 1
        

        if ct == 1:
            print('YES')

        else:
            print('NO')

solve()