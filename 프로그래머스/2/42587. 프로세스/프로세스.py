from collections import deque  # 덱 소환!

def solution(priorities, location):
    queue = deque()
    for i in range(len(priorities)):
        queue.append([priorities[i], i]) 
        
    answer = 0
    
    while True:
        current = queue.popleft()
        
        # 3. 나보다 중요한 게 있는지 하나씩 뒤져보기 (직관적인 for문)
        higher = False
        for q in queue:
            if current[0] < q[0]:
                higher = True
                break
                
        # 4. 판별 결과에 따른 행동
        if higher == True:
            # 나보다 중요한 놈이 있었으니 맨 뒤로 다시 줄 서기
            queue.append(current)
            
        else:
            # 내가 제일 중요하므로 실행!
            answer += 1
            if current[1] == location:
                return answer