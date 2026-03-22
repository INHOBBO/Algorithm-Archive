def solution(new_id):
    # 1단계: 소문자 치환
    answer = new_id.lower()
    
    # 2단계: 허용되지 않은 문자 제거
    result = ""
    for char in answer:
        if char.isalnum() or char in "-_.":
            result += char
    answer = result
    
    # 3단계: 마침표(.)가 2번 이상 연속되면 하나로 치환
    while '..' in answer:
        answer = answer.replace('..', '.')
        
    # 4단계: 마침표(.)가 처음이나 끝에 있으면 제거
    answer = answer.strip('.')
    
    # 5단계: 빈 문자열이라면 "a" 대입
    if not answer:
        answer = "a"
        
    # 6단계: 16자 이상이면 자르고, 마지막 마침표 제거
    if len(answer) >= 16:
        answer = answer[:15].rstrip('.')
        
    # 7단계: 2자 이하라면 마지막 문자를 길이가 3이 될 때까지 반복
    while len(answer) <= 2:
        answer += answer[-1]
        
    return answer