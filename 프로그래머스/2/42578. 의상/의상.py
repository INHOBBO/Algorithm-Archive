def solution(clothes):
    clothes_dic = {}
    
    for cloth in clothes:
        kind = cloth[1]
        clothes_dic[kind] = clothes_dic.get(kind, 0) + 1
        
    answer = 1
    for value in clothes_dic.values():
        answer *= (value + 1)
        
    return answer-1
    