# 거스름돈 개수 적게하기

money = int(input())
ex = [500, 100, 50, 10, 5, 1]

ex_money = 1000-money

bill = 0
i = 0
while ex_money != 0:
    bill += ex_money // ex[i] # 620 // 500 = 1
    ex_money = ex_money % ex[i] # 120
    
    i += 1

print(bill)