def solve(A,n,k):
    mx = max(A)
    base_score = 0
    mn = min(A)

    for i in range(len(A)):
        base_score += mx - A[i]

    if k < base_score: # impossible
        return -1
    
    diff = k - base_score
    new_max = diff // n + mx

    A.sort()

    score = 0

    for i in range(1,n):
        score += (new_max - A[i])
        
    return score - (A.count(mn) - 1)
   

t = int(input())
for _ in range(t):
    n,k = map(int,input().split())
    A = list(map(int,input().split()))
    print(solve(A,n,k))


