from collections import defaultdict,deque
t = int(input())
 
for _ in range(t):
    n,k = map(int,input().split())
    arr = list(map(int,input().split()))
 
    modulo = defaultdict(int)
    mx = 0
    for val in arr: #{1, 17: 1,,})
        rm = val % k
        if rm == 0:
            continue
        diff = k - rm
        modulo[diff] += 1
 
    q = deque(list(modulo.items()))
    while q:
        key,count = q.popleft()
    
        mx = max(mx,key + 1)
        if count > 1:
            q.append((key + k,count - 1))
 
    # print(modulo)
    print(mx)