def solve():
    n, k = map(int,input().split())
    nums = list(map(int,input().split()))
    st = [set() for _ in range(n)]
    ans = [0] * n
    curr = 0
    for i in range(n):
        assigned = False
        target = nums[i]
        for j in range(n):
            nxt = (curr + j) % k # we have to make sure this updates
            if target not in st[nxt]: # we can assigne
                ans[i] = (nxt + 1)
                st[nxt].add(target)
                assigned = True
                curr = (nxt + 1)  % k
                break
        
        if not assigned:
            return False, ans
        
    return True, ans


flag, ans = solve()
if flag:
    print("YES")
    print(*ans)

else:
    print('NO')
    # print()



