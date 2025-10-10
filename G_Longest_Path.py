from collections import defaultdict,deque
n,m = map(int,input().split())

graph = defaultdict(list)
in_degree = [0] * (n + 1)
queue = deque()
distance = [0] * (n + 1)
for _ in range(m):
    u,v = map(int,input().split())
    graph[u].append(v)
    in_degree[v] += 1

for i in range(1,n + 1):
    if in_degree[i] == 0:
        queue.append(i)


while queue:
    node = queue.popleft()
    
    for child in graph[node]:
        in_degree[child] -= 1

        if in_degree[child] == 0: #free
            distance[child] = distance[node] + 1
            queue.append(child)

print(max(distance))
