from collections import deque
import math # ceil 사용

def solution(progresses, speeds):
    answer = []
    progresses = deque(progresses)
    speeds = deque(speeds)
    
    while progresses:
        days = math.ceil((100-progresses[0]) / speeds[0])

        count = 0
        while progresses and (progresses[0] + days*speeds[0] >= 100):
            progresses.popleft()
            speeds.popleft()
            count += 1
        
        answer.append(count)
        
    
    return answer