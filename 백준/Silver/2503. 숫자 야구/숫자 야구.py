import sys
from itertools import permutations

input = sys.stdin.readline

n = int(input())
questions = [list(map(int, input().split())) for _ in range(n)]

# 1. 1~9까지 서로 다른 3자리 숫자의 모든 경우의 수를 생성합니다 (504개)
# 결과 예시: ('1', '2', '3'), ('1', '2', '4') ...
candidates = list(permutations(['1', '2', '3', '4', '5', '6', '7', '8', '9'], 3))

# 2. 민혁이의 질문을 하나씩 꺼내어 검사합니다.
for q_num, q_strike, q_ball in questions:
    q_num_str = str(q_num)
    survivors = [] # 이번 질문의 조건을 통과한 생존자들만 모을 리스트
    
    # 3. 504개의 후보(점점 줄어듦)를 하나씩 검증합니다.
    for cand in candidates:
        strike = 0
        ball = 0
        
        # 4. 후보 숫자와 민혁이의 질문 숫자를 비교해 스트라이크/볼을 판별합니다.
        for i in range(3):
            if cand[i] == q_num_str[i]:        # 위치와 숫자가 모두 같으면 스트라이크!
                strike += 1
            elif q_num_str[i] in cand:         # 위치는 다르지만 숫자가 존재하면 볼!
                ball += 1
                
        # 5. 영수의 대답과 정확히 일치하는 후보만 살아남습니다.
        if strike == q_strike and ball == q_ball:
            survivors.append(cand)
            
    # 생존자 리스트로 후보군을 교체하고, 다음 질문으로 넘어갑니다.
    candidates = survivors

# 6. 모든 질문을 통과하고 끝까지 살아남은 후보의 개수가 정답!
print(len(candidates))