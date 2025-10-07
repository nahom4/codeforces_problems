n = int(input())
a = list(map(int,input().split()))
b = list(map(int,input().split()))
 
ans = []
for i in range(n): 
    sub_array = b[i : ]
    f_b = sub_array.index(a[i]) + i
    for j in range(f_b,i,-1):
        b[j],b[j - 1] = b[j - 1],b[j]
        ans.append((j - 1,j))
 
# print(a)
print(len(ans))
for val in ans:
    print(val[0] + 1,val[1] + 1)