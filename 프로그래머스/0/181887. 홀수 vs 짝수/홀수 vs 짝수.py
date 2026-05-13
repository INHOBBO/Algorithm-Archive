def solution(num_list):
    odd = []
    even = []
    
    for i in range(len(num_list)):
        if i % 2 == 0: # i: 0, 2, 4, 6 ... 짝수. 여기선 홀수라고 생각해야함
            odd.append(num_list[i])
        elif i % 2 == 1:
            even.append(num_list[i])
    
    if sum(odd) == sum(even):
        return sum(odd)
    else:
        return max(sum(odd), sum(even))
    