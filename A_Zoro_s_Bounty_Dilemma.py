n = int(input())
for _ in range(n):
    s = input()
    if s.count('=') == len(s):
        print('=')
        continue

    idx = s.index('<')

    if '>' in s[idx : ]:
        print('?')

    else:
        for i in range(len(s)):
            if s[i] == '=':
                continue
            else:
                print(s[i])
                break





