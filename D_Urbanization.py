def solve():
    n,n1,n2 = map(int,input().split())
    array = list(map(int,input().split()))
    array.sort(reverse=True)
    mx = max(n1,n2)
    mn = min(n1,n2)
    
    ans = (sum(array[: mn]) / mn) + (sum(array[mn : mn + mx]) / mx)

    return ans

print(solve())