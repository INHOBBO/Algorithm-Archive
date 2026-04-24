from collections import Counter

def solution(participant, completion):
    loser = Counter(participant) - Counter(completion)
    return list(loser.keys())[0]