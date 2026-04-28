import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())

graph = [list(map(int, input().rstrip())) for _ in range(n)]

# 상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    Q = deque([(x, y)])

    while Q:
        cx, cy = Q.popleft()
        
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < n and 0 <= ny < m:
                if graph[nx][ny] == 1:
                    graph[nx][ny] = graph[cx][cy] + 1
                    Q.append((nx, ny))

    return graph[n-1][m-1]

print(bfs(0, 0))
