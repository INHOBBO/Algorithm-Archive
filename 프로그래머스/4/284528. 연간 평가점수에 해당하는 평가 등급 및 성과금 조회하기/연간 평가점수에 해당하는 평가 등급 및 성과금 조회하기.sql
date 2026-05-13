# 회사 부서 정보 테이블 HR_DEPARTMENT
# 회사 사원 정보 테이블 HR_EMPLOYEES
# 2022년 사원 평가 정보 테이블 HR_GRADE

# 사원별 성과금 정보 조회
# 사번 오름차순

SELECT E.EMP_NO, E.EMP_NAME,
        (
        CASE
        WHEN AVG(G.SCORE) >= 96 THEN 'S'
        WHEN AVG(G.SCORE) >= 90 THEN 'A'
        WHEN AVG(G.SCORE) >= 80 THEN 'B'
        ELSE 'C'
        END
        ) AS GRADE, 	
        E.SAL * (
        CASE
        WHEN AVG(G.SCORE) >= 96 THEN 0.2
        WHEN AVG(G.SCORE) >= 90 THEN 0.15
        WHEN AVG(G.SCORE) >= 80 THEN 0.1
        ELSE 0
        END
        ) AS BONUS
FROM HR_DEPARTMENT AS D
JOIN HR_EMPLOYEES AS E ON D.DEPT_ID = E.DEPT_ID
JOIN HR_GRADE AS G ON E.EMP_NO = G.EMP_NO
GROUP BY E.EMP_NO
ORDER BY E.EMP_NO