def solution(n):
    # 역발상! 거꾸로 가자.. 짝수면 //2 홀수면 -1
    jump = 0
    while n > 0:
        if n % 2 == 0:
            n //= 2
        else:
            n -= 1
            jump += 1
    
    return jump