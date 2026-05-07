def solution(numbers):
    answer = []
    
    for i in range(len(numbers)):
        for j in range(1, len(numbers)):
            if i == j or numbers[i] + numbers[j] in answer:            
                continue
            answer.append(numbers[i] + numbers[j])
    
    answer.sort()
    
    return answer