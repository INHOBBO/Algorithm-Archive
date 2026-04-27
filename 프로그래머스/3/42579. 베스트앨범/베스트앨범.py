def solution(genres, plays):
    answer = []
    
    # 모든 장르 정보를 하나로 담을 통합 딕셔너리
    dic = {}
    
    # 1. 딕셔너리에 데이터 채워 넣기
    for i, (g, p) in enumerate(zip(genres, plays)):
        # 처음 보는 장르라면 초기 폴더 구조를 만들어 줍니다.
        if g not in dic:
            dic[g] = [0, []]  # [총 재생 횟수, 곡 목록 리스트]
            
        # 총 재생 횟수 누적
        dic[g][0] += p
        # 곡 정보(재생 횟수, 고유 번호) 추가
        dic[g][1].append((p, i))
        
    # 2. 장르 정렬하기 (총 재생 횟수 기준 내림차순)
    # dic.items()는 ('pop', [3100, [(600, 1), (2500, 4)]]) 형태가 됩니다.
    # 따라서 x[1][0]은 3100(총 재생 횟수)을 가리킵니다.
    sorted_genres = sorted(dic.items(), key=lambda x: x[1][0], reverse=True)
    
    # 3. 정렬된 장르를 돌면서 앨범에 2곡씩 뽑아 넣기
    for genre, data in sorted_genres:
        songs = data[1] # 해당 장르의 곡 목록 리스트 꺼내기
        
        # 앞서 배웠던 다중 조건 정렬! (재생 횟수 내림차순, 고유 번호 오름차순)
        sorted_songs = sorted(songs, key=lambda x: (-x[0], x[1]))
        
        # 최대 2곡까지만 정답에 담기
        for i in range(min(len(sorted_songs), 2)):
            answer.append(sorted_songs[i][1])
            
    return answer