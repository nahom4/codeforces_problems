def solve(n,a,b):
    
    last = float("-inf")
    for i in range(n): 
        mn  =  min(a[i], b - a[i])
        mx = max(a[i], b - a[i])
        a[i] = mn  # small 
        if mn >= last:
            a[i] = mn
        else:
            a[i] = mx

        last = a[i]
      
    
    return a == sorted(a)


t = int(input())

for _ in range(t):
    n,_ = map(int,input().split())
    a = list(map(int,input().split())) 
    b = int(input())
    if solve(n,a,b):
        print('YES')
    else:
        print('NO')    
