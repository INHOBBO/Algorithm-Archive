n = int(input())

bags = 0

while n >= 0:
	if n % 5 == 0: # 5의 배수라면 가장 최선
		bags += (n // 5) # 몫 연산자 사용 (n/5시 .0)
		print(bags)
		break
	else: # 5의 배수가 아니라면 5의 배수가 될때까지!
		n -= 3
		bags += 1
	
	if n < 0:
		print(-1)
		