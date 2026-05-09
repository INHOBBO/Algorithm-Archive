# 학생 번호는 체격 순. 앞 뒤로만 체육복 빌려줄 수 있음
# n 전체 학생 수, lost 도난 당한 학생 리스트, reserve 여벌 옷 가진 학생 리스트
# 체육복 있는 최대 학생 수 구하기

def solution(n, lost, reserve):
    
    # 공통으로 있는 요소 제거
    reserve_set = set(reserve) - set(lost) # 여분 줄 준비된 애들 [1,3,5]
    lost_set = set(lost) - set(reserve) # 도난 당하고 여분도 없는 애들 [2,4]
    
    # 앞에 학생만 생각
    for i in reserve_set: # [1,3,5]
        if i-1 in lost_set: # [2,4]
            lost_set.remove(i-1)
        elif i+1 in lost_set:
            lost_set.remove(i+1)
    
    return n-len(lost_set)
            
        