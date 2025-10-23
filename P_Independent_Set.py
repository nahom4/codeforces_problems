from collections import defaultdict,deque
n = int(input())

# graph = defaultdict(list) # this is bad wright
graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
dp = [[1] * (n + 1), [1] * (n + 1)]
MOD = (10 ** 9 + 7)
# print(dp)
# TLE how do I improve this? 
queue = deque()
for _ in range(n - 1):
    u,v = map(int,input().split())
    graph[u].append(v)
    graph[v].append(u) #since it's a tree 

    indegree[u] += 1
    indegree[v] += 1

for i in range(n + 1):
    if indegree[i] == 1:
        dp[0][i] = 1 #mark the black ones
        queue.append(i)
    
# print(queue)
node = None
# TLE Is good right
visited = [False] * (n + 1)
while queue: # do we need a set? I don't think so 
    node = queue.popleft()
    # print(node)
    visited[node] = True
    for child in graph[node]:

        indegree[child] -= 1
        if visited[child]:
            continue
        # print(child,'child')
        # let's avoid this? how? 
        # so what's going on here? if it get's zero we don't want to do anything
        # for sure the issue is the unnessary calcuation that is happening here right
        # when should it happen? so edge count is a bad stuff we could have visited offcourse
        dp[0][child] *= dp[1][node] % MOD  
        dp[1][child] *= (dp[0][node] + dp[1][node]) % MOD 
        # print(dp)
        # how should I handle the visited ones? visitedd
        if indegree[child] == 1:# you should only add it if 
            queue.append(child)
            

# print(dp)
if node:
    print((dp[0][node] + dp[1][node]) % MOD)
else:
    print(2) # single node two way

# visited = set()
# def recursive(i,color):
  
#     paths = 0
#     # what if it's an edge
#     for child in graph[i]:
#         # there is only one way to reach to a child right
#         if child in visited:
#             continue
#         # but for the other paths it's combination right
#         # this is just complicated to implement by it's own right and since we get the dp aspect of 
#         # I thin I should just foucus on making the above immplementation work
#         if color == 1:
#             paths += dp(child,color)
#             paths += dp(child,1 - color)

#         else:
#             paths += dp(child, 1 - color)

#         visited.add(child)

#     return paths

