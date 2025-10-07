n = int(input())

def prime_factors(num):

    d = 2
    prime_factors_set = set()
    while d * d <= num:
        
        while num % d == 0:
            prime_factors_set.add(d)
            num //= d

        d += 1
    
    if num > 1:
        prime_factors_set.add(num)
        
    return prime_factors_set

# 10 almost prime, 6, 10
cnt_almost_prime = 0
for i in range(n + 1):
    prime_factors_set = prime_factors(i)

    if len(prime_factors_set) == 2:
        cnt_almost_prime += 1


print(cnt_almost_prime)
