def solution(rank, attendance):
    answer = []
    
    for i, r in enumerate(rank):
        if attendance[i] == True:
            answer.append([i, r])
    
    answer.sort(key=lambda x:x[1])
    
    return 10000*answer[0][0] + 100*answer[1][0] + answer[2][0]