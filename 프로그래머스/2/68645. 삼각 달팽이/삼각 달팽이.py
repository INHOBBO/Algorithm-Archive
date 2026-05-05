def solution(n):
    answer = [[0] * i for i in range(1, n+1)]
    
    row, col = -1, 0 # x는 행, y는 열
    num = 1
    
    for i in range(n):
        for _ in range(i, n): # 4개, 3개, 2개, 1개 이런 식으로
            if i % 3 == 0: # 아래로
                row += 1    
            elif i % 3 == 1: # 오른쪽
                col += 1
            elif i % 3 == 2: # 좌상단 대각선
                row -= 1
                col -= 1
            
            answer[row][col] = num
            num +=1
    
    return sum(answer, []) # 2차원 리스트 이어주는 꿀팁