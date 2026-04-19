from collections import Counter

def solution(k, tangerine):
    answer = 0
    
    count = Counter(tangerine)
    
    counts = sorted(count.values(), reverse=True)
    
    for c in counts:
        k -= c
        answer += 1
        
        if k <= 0:
            break
    
    return answer