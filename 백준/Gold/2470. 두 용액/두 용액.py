import sys
input = sys.stdin.readline

n = int(input())
liquid = list(map(int, input().split()))
liquid.sort()

left = 0
right = n-1

min_abs_sum = float('inf') # 최솟값 갱신하기 위해 무한대로 큰 값을 대입
answer = []

while left < right:
    cur_sum = liquid[left] + liquid[right]
    
    if abs(cur_sum) < min_abs_sum:
        min_abs_sum = abs(cur_sum)
        answer = [liquid[left], liquid[right]]

    if cur_sum == 0: # 가장 이상적인 상황
        break
        
    # 합이 0보다 작으면? -> 음수 값(왼쪽 정렬된 값)이 너무 큼, 값을 0에 가깝게 하기 위해 왼쪽 포인터 이동
    elif cur_sum < 0:
        left += 1
        
    # 합이 0보다 크면? -> 양수 기운이 너무 세니까, 값을 줄이기 위해 오른쪽 손가락 이동
    elif cur_sum > 0:
        right -= 1

# 최종적으로 가장 0에 가까웠던 두 용액 출력
print(answer[0], answer[1])