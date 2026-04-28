from collections import deque

n = int(input())
m = int(input())

# 그래프
graph = [[] for _ in range(n+1)]
visited = [0] * (n+1)

for i in range(m):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]

visited[1] = 1

q = deque([1])

while q:
    cur = q.popleft() # 덱에서 꺼내고 방문했는지 확인?
    for next in graph[cur]:
        if visited[next] == 0: # 방문안했다!
            q.append(next)
            visited[next] = 1


print(sum(visited)-1)