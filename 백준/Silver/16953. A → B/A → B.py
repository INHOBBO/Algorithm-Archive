# 문제
# 정수 A를 B로 바꾸려고 한다. 가능한 연산은 다음과 같은 두 가지이다.

# 2를 곱한다.
# 1을 수의 가장 오른쪽에 추가한다. 
# A를 B로 바꾸는데 필요한 연산의 최솟값을 구해보자.
import sys
input = sys.stdin.readline

A, B = map(int, input().split())

count = 0
while A != B: # greedy는 거꾸로 가는게 편함
    if A > B:
        print(-1)
        sys.exit(0)
    if B % 2 == 0: # 짝수라면
        B //= 2 # 162 > 81, 8 > 4 > 2
        count += 1 
    elif str(B)[-1] == '1': # 뒤에가 1이면 1제거
        B = int(str(B)[:-1]) # 81 > 8
        count += 1
    elif str(B)[-1] != '1' and B % 2 == 1: # 끝자리 1도 아니고 홀수라면
        print(-1)
        sys.exit(0)
print(count+1)