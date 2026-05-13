def solution(n):
    # 일단 전부 소수(True)라고 가정하고 리스트를 만들어요.
    sieve = [True] * (n + 1)
    
    # 0과 1은 소수가 아니니까 False!
    sieve[0] = sieve[1] = False
    
    # 2부터 n의 제곱근까지만 확인하면 됩니다.
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]: # i가 소수라면
            # i의 배수들을 전부 "넌 소수가 아니야(False)"라고 표시해요.
            for j in range(i*i, n + 1, i):
                sieve[j] = False
    
    # True로 남아있는 녀석들의 개수만 세면 끝!
    return sum(sieve)