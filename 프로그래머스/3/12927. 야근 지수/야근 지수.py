import heapq # 오름차순만 존재

def solution(n, works):
    answer = 0
    
    if sum(works) <= n:
        return 0
    
    # max heap만 존재하기 때문에 min heap으로 응용하기 위해 음수 값으로 변경
    works = [-i for i in works]
    
    # heap구조로 변경
    heapq.heapify(works)
    
    # 남은 일을 남은 시간으로 가장 큰 값들만 골라서 차감
    for i in range(n):
        t = heapq.heappop(works)
        t += 1
        heapq.heappush(works, t)
        
    for i in works:
        answer += i ** 2
        
    return answer