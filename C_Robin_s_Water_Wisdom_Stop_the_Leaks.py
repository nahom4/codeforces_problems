import math
n,a,b = map(int,input().split())
array = list(map(int,input().split()))

total = sum(array)
y = array[0] * a / b # 2 * 10 //8 2.ll
x = math.ceil(total - y) #
array.pop(0)
array.sort()
left = 0
running_sum = 0
ans = float("inf")
n = len(array)
# print(x)
for i in range(n):
    running_sum += array[i]
    # print(running_sum)
    while left < n and running_sum >= x:
        ans = min(ans,max(i - left + 1,0))
        running_sum -= array[left]
        left += 1
    
    if running_sum >= x:
         ans = min(ans,max(i - left + 1,0))


if ans == float("inf"):
    print(0)
else:
    print(ans)

    