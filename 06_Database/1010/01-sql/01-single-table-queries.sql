-- 01. Querying data
SELECT
  LastName
FROM
  employees;

SELECT 
    LastName, FirstName
FROM 
    employees;

SELECT
    *
FROM
    employees;

SELECT FirstName AS '이름'
FROM employees;

SELECT Name AS '이름', Milliseconds/60000 AS '재생 시간(분)'
FROM tracks;

-- 02. Sorting data
-- 오름차순
SELECT 
    FirstName
FROM 
    employees
ORDER BY
    FirstName ASC;

-- 내림차순
SELECT 
    FirstName
FROM 
    employees
ORDER BY
    FirstName DESC;


SELECT Country, City
FROM customers
ORDER BY Country DESC,
        City ASC;

SELECT Name, Milliseconds / 60000 AS '재생시간(분)'
FROM tracks
ORDER BY Milliseconds DESC;


-- NULL 정렬 예시
SELECT ReportsTo
FROM employees
ORDER BY ReportsTo;


-- 03. Filtering data
SELECT DISTINCT 
  Country
FROM 
  customers
ORDER BY 
  Country;

SELECT 
  LastName, FirstName, City
FROM 
  customers
WHERE 
  City != 'Prague';

SELECT 
    LastName, FirstName, Company, Country
FROM 
    customers
WHERE 
    Company IS NULL 
    AND Country = 'USA';

SELECT 
    Name, Bytes
FROM 
    tracks
WHERE 
    -- 100000 <= Bytes <= 500000;  -- 이건 안됨!! 
  
    -- Bytes BETWEEN 100000 AND 500000;
    -- AND 써도 됨!
    -- Bytes >= 100000
    -- AND Bytes <= 500000;

SELECT LastName, FirstName, Country
FROM customers
WHERE 
    Country IN ( LIKE 'Cana%', 'Germa%', 'France');
    -- Country = 'Canada'
    -- OR Country = 'Germany'
    -- OR Country = 'France';
    
SELECT LastName, FirstName
FROM customers
WHERE LastName LIKE '%son' ;

-- 자리수
SELECT 
    LastName, FirstName
FROM 
    customers
WHERE 
    FirstName LIKE'___a';


SELECT TrackId, Name, Bytes
FROM tracks
ORDER BY Bytes DESC
LIMIT 7;

-- 3개 상쇄시키고 4개 조회
-- LIMIT 3, 4;
-- LIMIT 4 OFFSET 3;




-- 04. Grouping data
SELECT Country, COUNT(*) 
FROM customers
GROUP BY Country;


SELECT 
  Composer, 
  AVG(Bytes)
FROM 
  tracks
GROUP BY 
  Composer
ORDER BY 
  AVG(Bytes) DESC;


SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
WHERE avgOfMinute < 10
GROUP BY Composer;

-- 에러

SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
WHERE avgOfMinute < 10
GROUP BY Composer; 
-- 이 순서로 GROUP BY 하면 오류 뜸


-- 에러 해결
SELECT Composer, AVG(Milliseconds / 60000) AS avgOfMinute
FROM tracks
GROUP BY Composer
HAVING avgOfMinute < 10;
-- having 써야 함