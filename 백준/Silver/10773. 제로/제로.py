k = int(input())

money_arr = []

for _ in range(k):
    money = int(input())
    if money == 0:
        money_arr.pop()
    else:
        money_arr.append(money)

print(sum(money_arr))