def solution(nums):
    n = len(nums)//2
    species_counts = len(set(nums))
    
    return min(n, species_counts)



# n마리 중 n/2마리까지 가져가도 좋음
# 종류에 따라 번호를 붙여 구분, 같은 종류는 같으 ㄴ번호
# 