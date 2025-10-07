from collections import Counter
def solve():
    s = input()
    ans  = max(Counter(s).values())

    def valid_counter(first,second):
        ct = 0
        found = False
        for i in range(len(s)):
            if found and s[i] == second:
                found = False
                ct += 2
            if s[i] == first:
                found = True
        
        return ct

    for i in range(10):
        for j in range(i + 1,10):
            ans = max(ans,valid_counter(str(i),str(j)))
            ans = max(ans,valid_counter(str(j),str(i)))

    return len(s) - ans

t = int(input())

for _ in range(t):
    print(solve())