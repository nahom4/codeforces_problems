p = input()
n = int(input())

barks = []
for _ in range(n):
    barks.append(input())

start = False
end = False

for b in barks:
    if b[1] == p[0]:
        start = True
    if b[0] == p[1]:
        end = True

if (start and end ) or p in barks:
    print('YES')

else:
    print("NO")



