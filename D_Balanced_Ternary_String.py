from collections import Counter
def forward(target,rep,req,string,ct):
    for i in range(len(string)):
        if string[i] == target:
            string[i] = rep
            req -= 1
            ct[target] -= 1
            ct[rep] += 1
        if req == 0:
            break


def backward(target,rep,req,string,ct):
    for i in range(len(string) - 1,-1,-1):
        if string[i] == target:
            string[i] = rep
            req -= 1
            ct[target] -= 1
            ct[rep] += 1
        if req == 0:
            break

one,two,three = '0','1','2'
def solve():
    n = int(input())
    s = list(input())
    ct = Counter(s)
    expec = n // 3
    # print(ct)

    if ct[three] > expec:
        #first we treat 1 then 2
        diff = ct[three] - expec
        if ct[one] < expec:
            req = min(expec - ct[one],diff)
            diff -= req
            forward(three,one,req,s,ct)

        if ct[two] < expec:
            req = min(expec - ct[two],diff)
            diff -= req
            forward(three,two,req,s,ct)

    if ct[two] > expec:
        diff = ct[two] - expec
        if ct[three] < expec:
            req = min(expec - ct[three],diff)
            diff -= req
            backward(two,three,req,s,ct)

        if ct[one] < expec:
            req = min(expec - ct[one],diff)
            diff -= req
            forward(two,one,req,s,ct)

    if ct[one] > expec:
        diff = ct[one] - expec
        if ct[three] < expec:
            req = min(expec - ct[three],diff)
            diff -= req
            backward(one,three,req,s,ct)

        if ct[two] < expec:
            req = min(expec - ct[two],diff)
            diff -= req
            backward(one,two,req,s,ct)

    return ''.join(s)

print(solve())
