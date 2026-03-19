def solution(name, yearning, photo):
    memory_point = dict(zip(name, yearning))
    
    answer = []
    
    for p in photo:
        point = 0
        for person in p:
            point += memory_point.get(person, 0)
            
        answer.append(point)
    
    return answer

