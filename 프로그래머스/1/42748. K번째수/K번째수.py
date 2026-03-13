def solution(array, commands):
    answer = []

    for command in commands:
        i = command[0]
        j = command[1]
        k = command[2]
        
        sorted_arr = sorted(array[i-1:j])
        answer.append(sorted_arr[k-1])
        
    return answer