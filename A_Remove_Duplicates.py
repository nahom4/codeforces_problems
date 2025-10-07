def solve():
    n = int(input())
    array = list(map(int,input().split()))

    #coollect all the duplicate indexes
    #add them to a new list
    tracker = {}
    for i in range(n):
        tracker[array[i]] = i

    numbers = list(tracker.keys())
    numbers.sort(key=( lambda x : tracker[x]))
    return numbers


numbers = solve()
print(len(numbers))
print(*numbers)