def solution(price, money, count):
    
    total_price = 0
    
    for i in range(1,count+1):    
        total_price += price*i
        
    if money - total_price >= 0:
        return 0 
    else:
        return abs(money - total_price)    