def solve():
    t = int(input())

    mapping = {"R" : "G", "G" : "B", "B" : "R"}
    def check_substring(curr,s,k,n):
        left = 0
        seen = set()
        mn = float("inf")
        for right in range(n):
            if s[right] != curr:
                seen.add(right)

            if right >= k:
                if left in seen:
                    seen.remove(left)

                left += 1

            if (right - left + 1) == k:
                mn = min(mn,len(seen))
            curr = mapping[curr]

        return mn


    for _ in range(t):
        n,k = map(int,input().split())
        s = input()
        mn_ans = float("inf")
        for char in ["R","G","B"]:
            mn_ans = min(check_substring(char,s,k,n),mn_ans)

        print(mn_ans)

solve()



