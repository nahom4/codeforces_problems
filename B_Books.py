def solve():
    n,t = map(int,input().split())
    books = list(map(int,input().split()))
    n = len(books)
    left = 0
    running_sum = 0
    ans = 0
    for i in range(n):
        running_sum += books[i]
        while running_sum > t:
            running_sum -= books[left]
            left += 1

        ans = max(ans, i - left + 1)

    return ans

print(solve())  #1 1 2  2 3 4

