def solution(s):
    nums = list(map(int, s.split()))
    
    max_value = max(nums)
    min_value = min(nums)
                
                
    return f"{min_value} {max_value}"