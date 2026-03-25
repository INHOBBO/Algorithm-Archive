def solution(targets):
    # 1. 종료 지점(e)을 기준으로 오름차순 정렬합니다.
    targets.sort(key=lambda x: x[1])
    
    answer = 0
    last_intercept = -1 # 마지막 요격 미사일의 위치 (초기값은 범위 밖으로 설정)
    
    for s, e in targets:
        # 2. 현재 미사일의 시작 지점(s)이 마지막 요격 지점보다 뒤에 있다면?
        if s >= last_intercept:
            # 기존 요격 미사일로는 맞출 수 없으므로 새로 하나 쏩니다.
            answer += 1
            # 3. 새로운 요격 위치를 현재 미사일의 종료 지점(e)으로 갱신합니다.
            # (실제로는 e보다 아주 약간 왼쪽인 e-0.5 같은 지점에 쏜다고 생각하면 됩니다.)
            last_intercept = e
            
    return answer