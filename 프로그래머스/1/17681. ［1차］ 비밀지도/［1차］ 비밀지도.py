def solution(n, arr1, arr2):
    answer = []
    
    for i in range(len(arr1)):
        combined = arr1[i] | arr2[i]
        
        combined_bin = bin(combined)[2:].zfill(n)
        
        answer.append(combined_bin.replace("0", " ").replace("1", "#"))
        
    return answer