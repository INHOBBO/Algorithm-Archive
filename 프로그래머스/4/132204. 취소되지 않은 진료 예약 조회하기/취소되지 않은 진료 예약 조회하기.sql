# 환자, 의사, 예약 테이블
# 2022-04-13이고 취소되지 않은 CS 진료 예약 내역 조회
# 취소되지 않았다? 1.아예 취소 안된 사람이거나, 2.취소했는데 '2022-04-13'이 아니거나
# 진료예약일시(APNT_YMD) 오름
SELECT A.APNT_NO, P.PT_NAME, P.PT_NO, D.MCDP_CD, D.DR_NAME, A.APNT_YMD
FROM APPOINTMENT AS A
JOIN PATIENT AS P ON P.PT_NO = A.PT_NO
JOIN DOCTOR AS D ON D.DR_ID = A.MDDR_ID
WHERE 
    D.MCDP_CD = 'CS'
    AND A.APNT_CNCL_YN = 'N' 
    AND DATE_FORMAT(A.APNT_YMD, '%Y-%m-%d') = '2022-04-13'
ORDER BY A.APNT_YMD