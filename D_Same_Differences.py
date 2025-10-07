from collections import defaultdict
t = int(input())

for _ in range(t):
    n = int(input())
    nums = list(map(int,input().split()))

    mp = defaultdict(int)
    ans = 0
    for i in range(n):
        key = nums[i] - i

        ans += mp[key]
        mp[key] += 1


    print(ans)

