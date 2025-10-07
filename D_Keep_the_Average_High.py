def solve():
    n = int(input())
    array = list(map(int,input().split()))
    x = int(input())

    array = list(map(lambda num : num -x,array))

    ct = 0
    i = 0
    array.append(0)
    while i in range(n - 1):
        if array[i] + array[i + 1] < 0:
            ct += 1
            i += 2

        elif array[i] + array[i + 1] + array[i + 2] < 0:
            ct += 1
            i += 3
        else:
            i += 1

    print(n - ct)



t = int(input())

for _ in range(t):
    solve()