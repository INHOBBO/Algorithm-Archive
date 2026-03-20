T = int(input())

for _ in range(T):
    # 거스름돈을 '센트' 단위 정수로 받습니다 (예: 124)
    money = int(input())
    
    # 동전 단위를 모두 '센트' 정수로 바꿉니다.
    exchange = [25, 10, 5, 1]
    
    for e in exchange:
        # 1. 해당 동전으로 거슬러 줄 수 있는 최대 개수
        count = money // e
        
        # 2. 남은 돈 갱신 (나머지 연산자 % 를 쓰면 훨씬 편해요!)
        money %= e
        
        # 3. 결과 출력
        print(count, end=" ")
    print() # 줄바꿈