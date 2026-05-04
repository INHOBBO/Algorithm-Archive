-- 1단계: 0부터 23까지 숫자를 만드는 가상 시간표 'HOURS' 만들기 HOUR 0~24 테이블 만들기
WITH RECURSIVE HOURS AS (
    SELECT 0 AS HOUR       -- 시작점: 0
    UNION ALL
    SELECT HOUR + 1        -- 이전 숫자에 1씩 더함
    FROM HOURS 
    WHERE HOUR < 23        -- 23이 될 때까지 반복!
)

-- 2단계: 만든 시간표(HOURS)에 실제 입양 기록(ANIMAL_OUTS)을 LEFT JOIN 하기
SELECT 
    H.HOUR, 
    COUNT(O.ANIMAL_ID) AS COUNT
FROM HOURS AS H
LEFT JOIN ANIMAL_OUTS AS O ON H.HOUR = HOUR(O.DATETIME)
GROUP BY H.HOUR
ORDER BY H.HOUR ASC;