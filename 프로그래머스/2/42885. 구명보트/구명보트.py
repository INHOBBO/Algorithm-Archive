def solution(people, limit):
    answer = 0
    people.sort() # 몸무게 순으로 오름차순 정렬
    
    # 투포인터 알고리즘
    left = 0                # 가장 가벼운 사람을 가리키는 손가락
    right = len(people) - 1 # 가장 무거운 사람을 가리키는 손가락
    
    while left <= right:
        # 가장 가벼운 사람과 무거운 사람의 합이 제한을 넘지 않는다면? -> 둘 다 태움!
        if people[left] + people[right] <= limit:
            left += 1   # 가벼운 사람은 탔으므로, 다음 가벼운 사람으로 이동
            right -= 1  # 무거운 사람도 탔으므로, 다음 무거운 사람으로 이동
            
        # 둘이 합쳐서 제한을 넘는다면? -> 무거운 사람 혼자 태움!
        else:
            right -= 1  # 무거운 사람만 혼자 타고 출발, 다음 무거운 사람으로 이동
            
        # 어떻게 타든 배는 한 대씩 출발하므로 보트 개수 +1
        answer += 1     
        
    return answer