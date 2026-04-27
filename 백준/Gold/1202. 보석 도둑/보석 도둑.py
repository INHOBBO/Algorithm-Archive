import sys
import heapq

# 1. 입력받기 (sys.stdin.readline으로 시간 단축)
input = sys.stdin.readline
n, k = map(int, input().split())

jewels = []
for _ in range(n):
    weight, value = map(int, input().split())
    jewels.append((weight, value))
    
bags = []
for _ in range(k):
    bags.append(int(input()))

# 2. 보석과 가방 정렬 (둘 다 오름차순)
jewels.sort()
bags.sort()

answer = 0
temp_jewels = [] # 들어갈 수 있는 보석의 '가격'을 모아둘 최대 힙

# 보석을 가리키는 인덱스 (투 포인터와 비슷한 역할)
jewel_idx = 0

# 3. 가장 작은 가방부터 순서대로 확인
for bag in bags:
    
    # 현재 가방의 용량(bag)보다 가볍거나 같은 보석은 전부 힙에 넣기
    while jewel_idx < n and jewels[jewel_idx][0] <= bag:
        # 최대 힙을 구현하기 위해 가격에 -를 붙여서 push!
        heapq.heappush(temp_jewels, -jewels[jewel_idx][1])
        jewel_idx += 1 # 힙에 넣은 보석은 다음번엔 건너뛰기 위해 인덱스 증가
        
    # 힙에 보석이 하나라도 들어있다면?
    if temp_jewels:
        # 가장 비싼 보석의 가격을 꺼내서(다시 -를 붙여 양수로 복구) 정답에 더하기
        answer -= heapq.heappop(temp_jewels)

print(answer)