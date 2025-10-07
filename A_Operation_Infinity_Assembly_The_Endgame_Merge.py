def solve():
    t = int(input())
    for _ in range(t):
        n, m, k = map(int, input().split())
        a = sorted(input())
        b = sorted(input())

        a_ptr, b_ptr = 0, 0
        a_count, b_count = 0, 0
        result = []

        while a_ptr < n and b_ptr < m:
            if (a_count < k and a[a_ptr] <= b[b_ptr]) or b_count >= k:
                result.append(a[a_ptr])
                a_ptr += 1
                a_count += 1
                b_count = 0
            else:
                result.append(b[b_ptr])
                b_ptr += 1
                b_count += 1
                a_count = 0

        print("".join(result))

solve()
