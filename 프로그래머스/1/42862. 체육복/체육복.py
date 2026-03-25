# def solution(n, lost, reserve):
#     _reserve = list(set(reserve)-set(lost))
#     _lost = list(set(lost)-set(reserve))
    
#     for r in _reserve:
#         if r-1 in _lost:
#             _lost.remove(r-1)
#         elif r+1 in _lost:
#             _lost.remove(r+1)
            
#     return n-len(_lost)


def solution(n, lost, reserve):
    answer = 0
    std = [1] * (n+1)
    
    for i in lost:
        std[i] = 0
        
    reserve.sort()
    
    for i in reserve:
        if i in lost:
            std[i] = 1
        elif std[i-1] == 0:
            std[i-1] = 1
        elif i+1 <= n and std[i+1] == 0:
            std[i+1] = 1
    
    answer = std.count(1)
    
    return answer-1