def solution(arr):
    # 세로 길이(행의 개수)와 가로 길이(열의 개수) 구하기
    num_rows = len(arr)
    num_cols = len(arr[0])
    
    # 1. 행(세로)이 열(가로)보다 많을 때 -> 각 행의 끝에 0을 추가
    if num_rows > num_cols:
        diff = num_rows - num_cols # 부족한 열의 개수
        for row in arr:
            # 부족한 개수만큼 0을 만들어서 행의 끝에 이어 붙임
            row.extend([0] * diff)
            
    # 2. 열(가로)이 행(세로)보다 많을 때 -> 바닥에 새로운 0 배열을 추가
    elif num_cols > num_rows:
        diff = num_cols - num_rows # 부족한 행의 개수
        for _ in range(diff):
            # 가로 길이만큼 0으로 채워진 새로운 행을 바닥에 추가
            arr.append([0] * num_cols)
            
    # 길이가 같으면 if문에 걸리지 않고 그대로 원본이 반환됨
    return arr