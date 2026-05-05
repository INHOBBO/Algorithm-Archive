def solution(order):
    stack = [] # 보조 벨트
    box_index = 0

    for box in range(1, len(order)+1):
        stack.append(box)
        
        # stack이 비어있지 않고 가장 위에 있는 상자가 원하는 인덱스라면?
        while stack and stack[-1] == order[box_index]:
            stack.pop()
            box_index += 1
    return box_index
        