
def is_reproducible():
    max_number = (10 ** 6 + 1)
    ans = [False] * max_number
    for i in range(500):
        for j in range(500):
            valid_number = (2020 * (i + j) + i)
            if valid_number >= max_number:
                continue

            ans[valid_number] = True

    return ans

t = int(input())
ans = is_reproducible()
for _ in range(t):
    n = int(input())
    if ans[n]:
        print("YES")
    else:
        print('NO')