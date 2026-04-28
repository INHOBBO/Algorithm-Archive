from collections import deque

# 1. 입력 받기
n = int(input())
# 지도 정보를 숫자로 변환해서 리스트에 담기
graph = [list(map(int, input())) for _ in range(n)]
visited = [[False] * n for _ in range(n)]

# 상, 하, 좌, 우 방향 이동을 위한 좌표 (국룰 코드!)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque([(x, y)])
    visited[x][y] = True
    count = 1  # 현재 단지의 집 개수 (시작점 포함)
    
    while queue:
        cx, cy = queue.popleft()
        
        # 상하좌우 4방향 확인
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]
            
            # 지도를 벗어나지 않고, 집이 있으며, 아직 방문하지 않았다면?
            if 0 <= nx < n and 0 <= ny < n:
                if graph[nx][ny] == 1 and not visited[nx][ny]:
                    visited[nx][ny] = True
                    queue.append((nx, ny))
                    count += 1
    return count

# 모든 칸을 돌면서 단지 찾기
result = []
for i in range(n):
    for j in range(n):
        # 집이 있고 아직 방문 안 한 곳 발견!
        if graph[i][j] == 1 and not visited[i][j]:
            # 그 단지의 집 개수를 구해서 리스트에 담기
            result.append(bfs(i, j))

# 결과 출력 (오름차순 정렬)
result.sort()
print(len(result)) # 단지 수
for c in result:
    print(c) # 각 단지의 집 수