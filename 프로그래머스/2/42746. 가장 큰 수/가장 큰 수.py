def solution(numbers):
    
    num = list(map(str, numbers)) # 정수 리스트를, 문자열 리스트로
    num.sort(key = lambda x: x*3, reverse=True)
        
    answer = "".join(num)
    return str(int(answer))