def solve():
    n,m = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort(reverse=True)
    start = array[0] + 1
    end = m - array[0] 
    flag = True
    if start >= end:
        flag = False
    #[0]   -3 -2 -1
    for i in range(1,n):
        if start >= end:
            flag = False

        start += array[i] + 1

    if flag:
        return 'YES'
    else:
        return 'NO'




t = int(input())

for _ in range(t):
    print(solve())