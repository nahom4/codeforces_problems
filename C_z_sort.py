def solve():
    n = int(input())
    array = list(map(int,input().split()))

    ans = [0] * n
    array.sort()
    right = 0 
    valid = True

    for i in range(0,n,2):
        ans[i] = array[right]
        right += 1

    for i in range(1,n,2):
        ans[i] = array[right]
        right += 1
        if i + 1 < n and ans[i + 1] > ans[i]:
            valid = False
        
        if ans[i - 1] > ans[i]:
            valid = False

    if valid:
        print(*ans)
    else:
        print('Impossible')

solve()


