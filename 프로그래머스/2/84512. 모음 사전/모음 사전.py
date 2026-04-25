def solution(word):
    answer = 0

    counts = [781, 156, 31, 6, 1]

    vowels_dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
    for idx, alpha in enumerate(word):
        answer += vowels_dic[alpha] * counts[idx] + 1
    
    return answer