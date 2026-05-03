import heapq

def solution(n, edge):    
    # 1. 그래프 및 최단거리 테이블 초기화
    graph = [[] for _ in range(n+1)]
    distance = [float('inf')] * (n+1)
    
    # 2. 양방향 간선 정보 입력
    for a, b in edge:      # append(도착 노드, 가중치)
        graph[a].append((b, 1)) # a에서 b노드까지 가중치는 1
        graph[b].append((a, 1)) # 양방향 간선!

    def dijkstra(start):
        q = [] # q (거리, 시작 노드)
        heapq.heappush(q, (0, start))
        distance[start] = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distance[now] < dist:
                continue
            
            # 현재 노드와 연결된 다른 노드들 확인
            for next_node, weight in graph[now]:
                cost = dist + weight
                if cost < distance[next_node]:
                    distance[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
                    
    dijkstra(1)
    
    valid_distances = [d for d in distance[1:] if d != float('inf')]
    max_dist = max(valid_distances)
    
    return valid_distances.count(max_dist)