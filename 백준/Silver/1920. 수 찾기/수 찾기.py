n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
a.sort()

for num in b:
	lt, rt = 0, n-1
	isExist = False
	
	# 이분탐색
	while lt <= rt:
		mid = (lt + rt) // 2 # 몫 연산자
		if num == a[mid]:
			isExist = True
			print(1)
			break
		elif num > a[mid]:
			lt = mid + 1
		else:
			rt = mid - 1
	
	if not isExist:
		print(0)