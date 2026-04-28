import sys
n = int(input())

words = [list(input()) for _ in range(n)]

for char in words: # (())())
    stack = []
    for cha in char: # ( 
        if cha == '(':
            stack.append(cha) # stack ( (
        elif cha == ')':
            if not stack: # 스택이 비었다면
                stack = [1] # 스택 아무 값 채우기 (에러니까 "NO" 출력하게)
                break
            else:
                stack.pop() # 안 비었으면 그냥 pop()
    if len(stack) == 0:
        print("YES")
    else:
        print("NO")
        