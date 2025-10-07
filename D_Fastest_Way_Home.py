from collections import defaultdict
import heapq

n,m = map(int,input().split())
graph = defaultdict(list)
distances = [float('inf')] * (n + 1)
path = defaultdict(int) 

for _ in range(m):
    u,v,w = map(int,input().split())
    graph[u].append((v,w))
    graph[v].append((u,w)) # undirected

heap = [(0,1)]

while heap:
    curr_w, node = heapq.heappop(heap)

    for child, child_w in graph[node]:

        if distances[child] > (child_w + curr_w):
            heapq.heappush(heap,(child_w + curr_w, child))
            distances[child] = child_w + curr_w 
            path[child] = node

if not path[n]: # n is the target 
    print(-1)
else:
    ans = [n]
    curr = n
    while curr != 1:
        curr = path[curr]
        ans.append(curr)
        

    print(*ans[::-1])






