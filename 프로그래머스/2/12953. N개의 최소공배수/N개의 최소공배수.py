import math

def solution(arr):
    answer = arr[0]
    
    for n in arr[1:]:
        answer = (answer*n) // math.gcd(answer, n)
        
    return answer
        