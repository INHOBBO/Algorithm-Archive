n = int(input())

bags = 0

while n >= 0:
    if n % 5 == 0:
        bags += (n // 5)
        print(bags)
        break
    else:
        n -= 3
        bags += 1

    if n < 0:
        print(-1)