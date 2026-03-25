import heapq

def solution(scoville, K):
    answer = 0
    
    # 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

    heapq.heapify(scoville)
    
    while scoville[0] < K:
        f = heapq.heappop(scoville) # 제일 작은 값이 pop하면 먼저 빠짐!! 낮은게 1등
        s = heapq.heappop(scoville)
        t = f + s*2
        heapq.heappush(scoville, t) # s에다가 t?
        answer += 1
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer