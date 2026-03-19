from collections import Counter

def solution(participant, completion):
        
    one_per = Counter(participant)-Counter(completion)

    return (list(one_per.keys()))[0]