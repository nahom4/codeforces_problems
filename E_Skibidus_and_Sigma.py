def score(array):
    s_score = array[0]
    for i in range(1,len(array)):
        array[i] += array[i - 1]
        s_score += array[i]

    return s_score, array[-1]

def solve():
    n,m = map(int,input().split())
    sm_list = []
    ans = 0
    for _ in range(n):
        array = list(map(int,input().split()))
        sc,sm = score(array)
        sm_list.append(sm)
        ans += sc

    sm_list.sort(reverse=True)
    for i in range(n):
        curr = sm_list[i]
        ans += curr * (n - (i + 1)) * m

    return ans


t = int(input())
for _ in range(t):
    print(solve())