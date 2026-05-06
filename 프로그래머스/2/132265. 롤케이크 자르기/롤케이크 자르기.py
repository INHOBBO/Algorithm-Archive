from collections import Counter

def solution(topping):
    answer = 0
    # 1. 오른쪽 조각에 일단 모든 토핑을 다 몰아넣습니다 (개수를 셉니다)
    right_side = Counter(topping)
    # 2. 왼쪽 조각은 처음엔 비어있습니다 (종류만 체크하면 되니 set)
    left_side = set()
    
    # 3. 롤케이크를 앞에서부터 하나씩 왼쪽으로 옮깁니다
    for t in topping:
        # 왼쪽 세트에 토핑 추가
        left_side.add(t)
        # 오른쪽 딕셔너리에서 해당 토핑 개수 하나 감소
        right_side[t] -= 1
        
        # 만약 오른쪽에서 특정 토핑이 0개가 되면, 종류가 하나 줄어든 것이므로 삭제
        if right_side[t] == 0:
            del right_side[t]
            
        # 4. 왼쪽 세트의 크기(종류 수)와 오른쪽 딕셔너리의 크기(종류 수)를 비교
        if len(left_side) == len(right_side):
            answer += 1
            
    return answer