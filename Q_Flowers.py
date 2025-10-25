n = int(input())
h = list(map(int,input().split()))
a = list(map(int,input().split()))

# so we are going to use BIT to solve the problem

class BIT:
    def __init__(self):
        self.tree = [0] * (n + 1)

    
    def update(self,i,value): # Here we update the max right
        
        while i <= n: # This allows 1 indexed queries right zero indexed ones as well
            self.tree[i] = max(self.tree[i],value)
            i = i + (i & -i)

    def query(self,i): #
        mx = 0

        while i > 0:
            mx = max(mx, self.tree[i])
            i = i - (i & -i)

        return mx
    

# H goes from 0 to N right and this is what we will keep track of
bit = BIT()
ans = 0
for i in range(n):
    height,beauty = h[i],a[i]
    mx = bit.query(height)
    ans = max(ans,beauty + mx)
    bit.update(height,beauty + mx)


print(ans)
    





