n =int(input())
A,B,C = [],[],[]

for i in range(n):
    a,b,c = map(int,input().split())
    A.append(a)
    B.append(b)
    C.append(c)

a,b,c = A[0],B[0],C[0] #base case

for i in range(1, n):
    # for a check b and c
    curr_a = A[i] + max(b,c)
    curr_b = B[i] + max(a,c)
    curr_c = C[i] + max(a,b)

    a,b,c = curr_a,curr_b,curr_c

print(max(a,b,c))