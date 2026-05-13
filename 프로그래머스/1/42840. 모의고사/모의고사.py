# 1번 학생 채점 쭉, 몇개인지 ~

def solution(answers):
    answer = []
    score = [0, 0, 0]
    a1 = [1,2,3,4,5]
    a2 = [2,1,2,3,2,4,2,5]
    a3 = [3,3,1,1,2,2,4,4,5,5]
    
    for i in range(len(answers)):
        if answers[i] == a1[i%5]:
            score[0] += 1
        if answers[i] == a2[i%8]:
            score[1] += 1
        if answers[i] == a3[i%10]:
            score[2] += 1
    
    for idx, value in enumerate(score):
        if score[idx] == max(score):
            answer.append(idx + 1)
    

    return answer