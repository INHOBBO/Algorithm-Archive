def solution(elements):
    extended_elements = elements * 2
    
    result = set()
    
    for i in range(len(elements)):
        current_sum = 0
        for j in range(len(elements)):
            current_sum += extended_elements[i+j]
            result.add(current_sum)
            
    return len(result)  