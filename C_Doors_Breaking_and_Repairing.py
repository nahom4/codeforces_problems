import math
def solve():
    n,x,y = map(int,input().split())
    nums = list(map(int,input().split()))

    if x > y:
        return n
    target = 0
    for i in range(n):
        if nums[i] <= x:
            target += 1

    return math.ceil(target / 2)

print(solve())