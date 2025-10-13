n = int(input())
dishes = list(map(int, input().split()))

ct = [0] * 4
for dish_type in dishes:
    ct[dish_type] += 1


dp = [[[0.0 for _ in range(n + 2)] for _ in range(n + 2)] for _ in range(n + 2)]


for k in range(n + 1):
    for j in range(n + 1 - k):
        for i in range(n + 1 - k - j):
            if i == 0 and j == 0 and k == 0:
                continue

            denominator = float(i + j + k)
            
            numerator = float(n)
            
            if i > 0:
                numerator += i * dp[i - 1][j][k]
            if j > 0:
 
                numerator += j * dp[i + 1][j - 1][k]
            if k > 0:
                numerator += k * dp[i][j + 1][k - 1]

            dp[i][j][k] = numerator / denominator

c1, c2, c3 = ct[1], ct[2], ct[3]
print(f"{dp[c1][c2][c3]:.10f}")