import heapq

def solution(n, works):
    # 1. 모든 작업의 합보다 퇴근까지 남은 시간 n이 크면 피로도는 0입니다.
    if sum(works) <= n:
        return 0
    
    # 2. 최대 힙을 만들기 위해 모든 작업량을 음수로 바꿔서 힙에 넣습니다.
    # [4, 3, 3] -> [-4, -3, -3]
    max_heap = []
    for w in works:
        heapq.heappush(max_heap, -w)
        
    # 3. n시간 동안 가장 큰 작업량을 하나씩 꺼내서 1씩 줄입니다.
    for _ in range(n):
        # 가장 큰 값을 꺼냅니다 (음수이므로 가장 작은 값이 절댓값은 가장 큼)
        max_val = heapq.heappop(max_heap)
        
        # 작업량을 1 줄여서 다시 넣습니다 (음수이므로 1을 더하면 절댓값은 줄어듬)
        heapq.heappush(max_heap, max_val + 1)
        
    # 4. 남은 작업량들을 제곱하여 모두 더합니다.
    # 음수를 제곱해도 양수가 되므로 그대로 계산합니다.
    answer = sum(w**2 for w in max_heap)
    
    return answer