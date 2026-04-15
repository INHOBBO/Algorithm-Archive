def solution(number, limit, power):
    total_iron = 0 # 정답(필요한 총 철의 무게)을 담을 변수
    
    for i in range(1, number + 1):
        divisor_num = 0
        
        # 1. 제곱근까지만 반복 (int(i**0.5)는 i의 루트 값의 정수 부분입니다)
        for j in range(1, int(i**0.5) + 1):
            if i % j == 0:
                divisor_num += 1 # 짝꿍 중 작은 수 (예: 2)
                
                # 2. 짝꿍 중 큰 수 (예: 50)도 더해줍니다. 
                # 단, 10*10=100 처럼 같은 수일 때는 중복해서 더하면 안 됩니다.
                if j * j != i: 
                    divisor_num += 1 
        
        # 3. 약수 개수 제한 초과 검사
        if divisor_num > limit:
            divisor_num = power
            
        # 4. 총합에 누적
        total_iron += divisor_num
        
    return total_iron