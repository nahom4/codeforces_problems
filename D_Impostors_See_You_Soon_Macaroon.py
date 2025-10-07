def solve():
    n,k = map(int,input().split())
    s = input()

    end = n
    ct = 0
    ls = []
    trailing = 0
    for i in range(n - 1,-1,-1):
        if s[i] == 'L':
            ct += 1
        else:
            if not end == n:
                ls.append([ct,end])
            else:
                trailing = ct
            end = i
            ct = 0

    ls.sort()
    if trailing:
        ls.append([trailing, n])
    if ct:
        ls.append([end,ct])
    

    #let's update s
    # change the way 
    s = list(s)
    for ct,index in ls:
        if index == n:
            i = index - ct
            while k and ct:
                s[i] = 'W'
                k -= 1
                i += 1
                ct -= 1
        else:
            i = index - 1 
            while k and ct:
                s[i] = 'W'
                k -= 1
                i -= 1
                ct -= 1

    # calculate the new result
    total = 1 if s[0] == 'W' else 0
    for i in range(1,n):
        if s[i] == 'W' and s[i - 1] == 'W':
            total += 2

        if s[i] == 'W' and s[i - 1] != 'W':
            total += 1


    return total



t = int(input())
for _ in range(t):
    print(solve())