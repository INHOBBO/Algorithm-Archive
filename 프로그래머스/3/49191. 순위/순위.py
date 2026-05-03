import heapq

def solution(n, results):
    # 1. 그래프 초기화 (정방향, 역방향)
    graph = [[] for _ in range(n + 1)]
    reverse_graph = [[] for _ in range(n + 1)]
    
    for win, lose in results:
        graph[win].append((lose, 1))         # win -> lose (정방향)
        reverse_graph[lose].append((win, 1)) # lose -> win (역방향)

    # 2. 다익스트라 함수 (특정 그래프에서 도달 가능한 노드 수 반환)
    def dijkstra(start, target_graph):
        distances = [float('inf')] * (n + 1)
        distances[start] = 0
        q = [(0, start)]
        count = 0
        
        while q:
            dist, now = heapq.heappop(q)
            
            if distances[now] < dist:
                continue
            
            for next_node, weight in target_graph[now]:
                cost = dist + weight
                if cost < distances[next_node]:
                    distances[next_node] = cost
                    heapq.heappush(q, (cost, next_node))
                    count += 1 # 도달 가능한 새로운 노드를 찾을 때마다 카운트
        
        return count

    # 3. 모든 선수에 대해 조사
    answer = 0
    for i in range(1, n + 1):
        # (내가 이긴 사람 수) + (나를 이긴 사람 수)
        wins = dijkstra(i, graph)
        losses = dijkstra(i, reverse_graph)
        
        # 총합이 n-1이면 순위 확정!
        if wins + losses == n - 1:
            answer += 1
            
    return answer