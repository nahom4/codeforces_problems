
n,k = map(int,input().split())
grid = []
MOD = (10 ** 9 + 7)

for _ in range(n):
    grid.append(list(map(int,input().split())))

def multiply_matrices(A, B, n):
    """Performs (A @ B) % MOD using standard Python lists."""
    C = [[0] * n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            sum_val = 0
            for k in range(n):
                # Apply modulo during the sum to prevent overflow
                sum_val = (sum_val + A[i][k] * B[k][j]) % MOD
            C[i][j] = sum_val
    return C


result = [[0] * n for _ in range(n)]
for i in range(n):
        result[i][i] = 1
while k > 0:
   
    if k % 2: #odd
        result = multiply_matrices(result, grid,n)

    grid = multiply_matrices(grid,grid,n)

    k //= 2

ans = 0
for i in range(n):
    for j in range(n):
        ans += result[i][j]  # proly the issue is heref

print(ans % MOD)