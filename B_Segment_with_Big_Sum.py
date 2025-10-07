def solve():

    n,s = map(int,input().split())
    array = list(map(int,input().split()))

    running_sum = 0
    left = 0
    mn_window = float("inf")

    for right in range(n):
        # update running sum
        running_sum += array[right]

        #validate
        while running_sum - array[left] >= s: # 6 8 9
            running_sum -= array[left]
            left += 1

        #register 
        if running_sum >= s:
            mn_window = min(mn_window, right - left + 1)

    
    if mn_window == float("inf"):
        print(-1)
    else:
        print(mn_window)

solve()

