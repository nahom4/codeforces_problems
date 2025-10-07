def solve():
    n = int(input())
    s = input()
    ct_one = s.count("n")
    ct_z = s.count("z")

    number = ''
    number += '1' * ct_one
    number += '0' * ct_z
    print(*list(number))

solve()