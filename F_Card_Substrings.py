from collections import Counter
def solve():
    n,_ = map(int,input().split())
    s = input()
    cards = input()

    cards_count = Counter(cards) # {a : 2, b: 1}
    s_count = Counter()
    left = 0
    ans = 0

    
    for right in range(n): # aab
        # add the current value to your running variable
        s_count[s[right]] += 1  # {a : 1}
        # validate your window
        while s_count[s[right]] > cards_count[s[right]]: # the window is invalid
            s_count[s[left]] -= 1
            left += 1

        # update your result
        ans += (right - left + 1) # add all the valid windows

    print(ans)


solve()
