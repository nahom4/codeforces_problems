def solve():
    n,x = map(int,input().split())
    array = list(map(int,input().split()))

    t = array.index(x)

    left, right = 0,n

    while right - left > 1:
        mid = left + (right - left) // 2

        if array[mid] <= x:
            left = mid
        
        else:
            right = mid

    return (t + 1,left + 1)

t = int(input())

for _ in range(t):
    print(1)
    print(*solve())