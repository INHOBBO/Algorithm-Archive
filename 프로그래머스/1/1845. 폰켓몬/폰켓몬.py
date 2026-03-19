def solution(nums):
    
    n = len(nums) // 2

    species_counts = len(set(nums))
    
    return min(n, species_counts)
