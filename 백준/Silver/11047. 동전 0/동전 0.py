# 준규가 가지고 있는 동전은 총 N종류이고, 각각의 동전을 매우 많이 가지고 있다.
# 동전을 적절히 사용해서 그 가치의 합을 K로 만들려고 한다.
# 이때 필요한 동전 개수의 최솟값을 구하는 프로그램을 작성하시오.
import sys
input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for i in range(n)]
# print(coins)
coins.sort(reverse=True)
# print(coins)

count = 0
for coin in coins: # 4200 % 50000
    count += k // coin
    k %= coin

print(count)