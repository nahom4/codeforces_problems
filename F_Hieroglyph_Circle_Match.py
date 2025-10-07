from collections import defaultdict


def solve():
    la,lb = map(int,input().split())
    a = list(map(int,input().split()))
    b = list(map(int,input().split()))

    mp = defaultdict(lambda: -1)
    for i in range(lb):
        mp[b[i]] = i

    final = [-1] * (2 * la + 1)
    for i in range(la):
        final[i] = mp[a[i]]
        if final[i] >= 0:
            final[i + la] = final[i]

    ans = 0


    # 1 3 5 2  1 3 5 2
    # 1 2 3 4 5 6 1 2 3 4 5 6

    # 3 3
    # 1 2 3 1 2 3  1 2
    # 3 2 1  3 2 1

    left = 0
    for right in range(2 * la):
        #if it's 
        if final[right] == -1: # N/a
            left = right + 1

        elif final[right - 1] > final[right]:
            left = right

        elif final[right] - final[left] >= lb: # full circle
            left = right

        ans = max(ans,right - left + 1) 

    print(ans)


solve()

