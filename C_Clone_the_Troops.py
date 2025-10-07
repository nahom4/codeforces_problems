def solve():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))

    #max sub array sum
    mx_sum = 0
    running_sum = 0

    for i in range(n):
        running_sum += array[i]
        mx_sum = max(mx_sum,running_sum)
        if running_sum < 0:
            running_sum = 0

    total_sum = sum(array)
    #mx_sum(2 + 4 + 8 + ... 2**k - 1)
    # 1 2 4
   
    total_sum += mx_sum * ((2 ** k  - 1))

    return (total_sum) % (10**9+7)


t = int(input())

for _ in range(t):
    print(solve())