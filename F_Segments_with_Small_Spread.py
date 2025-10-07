from collections import deque
def solve():
    n,k = map(int,input().split())
    array = list(map(int,input().split()))

    mx_queue = deque()
    mn_queue = deque()
    ans = 0
    left = 0
    for i in range(n):
        
        curr = array[i]
        #max
        while mx_queue and array[mx_queue[-1]] <= curr:
            mx_queue.pop()

        mx_queue.append(i)

        #min
        while mn_queue and array[mn_queue[-1]] >= curr:
            mn_queue.pop()

        mn_queue.append(i)

        #diff between the max and the min
        # print(mx_queue)
        # print(mn_queue)
        while array[mx_queue[0]] - array[mn_queue[0]] > k: #invalid
            if mx_queue[0] == left:
                mx_queue.popleft()

            if mn_queue[0] == left:
                mn_queue.popleft()
            
            left += 1

        ans += (i - left + 1)

    print(ans)
 

solve()