def solution(my_string):
    answer = []
    
    for string in my_string:
        if string.isdigit():
            answer.append(int(string))   
        answer.sort()
    return answer