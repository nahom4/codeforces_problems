t = int(input())
for _ in range(t):
    n = int(input())
    s = input()

    sign = 1
    ptr = 0
    mn,mx = float("inf"),float("-inf")

    for i in range(n): # 01110
        if i > 0 and s[i - 1] == s[i]: #equal
            sign *= -1

        else:
            ptr += sign

        mx = max(mx,ptr)
        mn = min(mn,ptr)

    print(mx - mn + 1)


