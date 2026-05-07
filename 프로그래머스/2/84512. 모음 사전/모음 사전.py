# def solution(word):
#     answer = 0

#     counts = [781, 156, 31, 6, 1]

#     vowels_dic = {'A':0, 'E':1, 'I':2, 'O':3, 'U':4}
    
#     for idx, alpha in enumerate(word):
#         answer += vowels_dic[alpha] * counts[idx] + 1
    
#     return answer

def solution(word):
    vowels = ['A', 'E', 'I', 'O', 'U']
    cnt = 0        # 지금 몇 번째 단어인지 세는 변수 (카운트!)
    answer = 0     # 우리가 찾고자 하는 단어의 순서

    def dfs(current):
        nonlocal cnt, answer
        
        # 1. 빈 문자열이 아니면 단어 하나를 찾은 것이므로 카운트 +1
        if current != "":
            cnt += 1 # ★ 여기가 바로 카운트 세는 곳!
            # 만약 지금 단어가 우리가 찾는 단어라면 정답 기록
            if current == word:
                answer = cnt
                return # 찾았으니 일단 멈춤!

        # 2. 길이가 5인 단어면 더 깊이 못 들어감 (유턴!)
        if len(current) == 5:
            return

        # 3. 다음 모음을 붙여서 더 깊게 들어감
        for v in vowels:
            if answer != 0: return # 이미 찾았으면 더 안 돌아도 됨
            dfs(current + v)

    dfs("") # 시작!
    return answer