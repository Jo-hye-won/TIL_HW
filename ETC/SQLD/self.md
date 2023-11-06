> 논리연산자는 SQL에 명시된 순서와 관계없이 __`() -> NOT -> AND -> OR`__
순으로 처리된다.

> 조건식에서 컬럼명은 일반적으로 좌측에 위치하지만 우측에 위치해도 정상적으로 동작

## SELECT 문의 논리적 수행 순서 
	: FROM -> WHERE -> GROUP BY -> HAVING -> SELECT -> ORDER BY

## GRADE 오름차순 하면?
	- 1등급 -> 2등급 -> 3등급 ...

> JOIN 되는 두 테이블에 모두 존재하는 컬럼의 경우
	컬럼명 앞에 반드시 테이블명이나 ALIAS를 명시해주어야 한다.

## OUTER JOIN 
- Oracle에서는 모든 행이 출력되는 테이블의 반대편 테이블의 옆에 (+) 기호를 붙여 작성

## STANDARD JOIN 
- ANSI JOIN, 표준 조인이라는 말이 더 많이 쓰임
- Oracle에서도 돌아가고 MySQL에서도 돌아가는 JOIN쿼리

### INNER JOIN
- Oracle에서는 JOIN 조건을 ON절을 사용해서 작성해야함

> `NON EQUI JOIN`의 경우 JOIN 컬럼이라도 서로 다른 값을 가질 수 있기 때문에
SELECT 절에서 A.COL1을 B.COL1으로 `대체할 수 없다.`

> `EQUI JOIN`의 경우에는 
SELECT 절에서 JOIN 컬럼인 A.COL1을 B.COL1로 `대체할 수 있다.` 

> NATURAL JOIN에는 ON절을 쓸 수 없다.
> JOIN 에서 USING절을 사용할 경우 USING 절로 정의된 컬럼 앞에는 별도의
	 테이블명이나 ALIAS를 표기할 수 없다.

👀 WHERE COL2 = NULL; 이라고 하면,
👀 NULL과의 연산 결과는 False이므로 조건값이 늘 거짓이 되어 아무 데이터도 출력되지 않는다.
👀 NULL은 IS NULL 아니면 IS NOT NULL로만 쓰인다


### NULLIF(인수1, 인수2)
- 인수1과 인수2가 같으면 NULL을 반환하고 같지 않으면 인수1을 반환해주는 함수이다. 
P. 156