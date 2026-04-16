import sys

# 1. N(행)과 M(열) 입력받기
n, m = map(int, sys.stdin.readline().split())

# 2. 보드의 색깔 상태 입력받기
board = []
for _ in range(n):
    board.append(sys.stdin.readline().strip())

# 칠해야 하는 최소 개수를 저장할 변수 (초기값은 아주 큰 수로 설정)
min_repaints = 64 # 8x8을 다 칠해도 최대 64칸이므로 64로 시작해도 충분합니다.

# 3. 8x8 쿠키 틀을 이동시키는 바깥쪽 루프 (슬라이딩 윈도우)
# 쿠키 틀이 벽을 뚫고 나가지 않게 범위를 n-7, m-7로 제한합니다.
for i in range(n - 7):
    for j in range(m - 7):
        
        # 현재 위치(i, j)에서 8x8 구역을 검사할 때 쓸 카운트 변수
        w_start_paint = 0 # W(흰색)로 시작하는 판과 비교할 때 칠할 개수
        b_start_paint = 0 # B(검은색)로 시작하는 판과 비교할 때 칠할 개수
        
        # 4. 8x8 쿠키 틀 안쪽을 한 칸씩 돋보기로 검사하는 안쪽 루프
        for a in range(i, i + 8):
            for b in range(j, j + 8):
                
                # 💡 좌표의 합(a+b)이 짝수인지 홀수인지로 체스판 패턴을 구별합니다.
                if (a + b) % 2 == 0:
                    # 짝수 칸은 맨 왼쪽 위(시작점)와 색이 무조건 같아야 함
                    if board[a][b] != 'W':
                        w_start_paint += 1
                    if board[a][b] != 'B':
                        b_start_paint += 1
                else:
                    # 홀수 칸은 맨 왼쪽 위(시작점)와 색이 무조건 달라야 함
                    if board[a][b] != 'B':
                        w_start_paint += 1
                    if board[a][b] != 'W':
                        b_start_paint += 1
                        
        # 5. 현재 구역에서 (W시작 판)과 (B시작 판) 중 더 적게 칠하는 걸 고름
        current_min = min(w_start_paint, b_start_paint)
        
        # 6. 지금까지 찾은 최솟값(min_repaints)과 비교해서 더 작으면 갱신!
        if current_min < min_repaints:
            min_repaints = current_min

print(min_repaints)