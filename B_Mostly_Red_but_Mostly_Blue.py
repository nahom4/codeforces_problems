def solve():
    t = int(input())
    for _ in range(t):
        n = int(input())
        array = list(map(int,input().split()))

        array.sort()
        prefix_array = list(array)
        for i in range(1,n):
            prefix_array[i] += prefix_array[i - 1]

        
        running_sum = 0
        prefix_array.append(0)
        flag = False
        for i in range(n - 1,-1,-1):
            #two possibilities add or skip
            #skip
            # i elements on the left
            # n - i - 1 elements on the right
            if i > (n - i - 1) and running_sum > prefix_array[i - 1]:
                flag = True
            
            running_sum += array[i]
            #add
            if i > (n - i) and running_sum > prefix_array[i - 1]:
                flag = True

        if flag:
            print('YES')
        else:
            print('NO')

solve()


        
