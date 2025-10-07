def solve():
    n,s = map(int,input().split())
    a = list(map(int,input().split()))

    running_sum = 0
    left = 0
    mx = 0

    #  4 3 6 8 9  s
    for right in range(n):
        #update the running sum
        running_sum += a[right]

        #validate
        while running_sum > s:
            running_sum -= a[left]
            left += 1

        #register
        mx = max(mx,right - left + 1)

    print(mx)

solve()

        