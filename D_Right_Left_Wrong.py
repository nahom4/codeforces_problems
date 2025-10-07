def solve():
    n = int(input())
    damage = list(map(int,input().split()))
    s = input()
    
    for i in range(1,n):
        damage[i] += damage[i - 1]

    left = 0
    right = n - 1
    running_sum = 0
    damage.append(0)

    # LLLLLLLL
    while left < right:
        while left < right and  s[left] != 'L':
            left += 1

        while left < right and  s[right] != 'R':
            right -= 1

        if left < right:
            running_sum += damage[right] - damage[left - 1]
        left += 1
        right -= 1

    return running_sum
t = int(input())
for _ in range(t):
    print(solve())