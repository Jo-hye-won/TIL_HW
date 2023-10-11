-- DML
DROP TABLE articles;

CREATE TABLE articles(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    -- 이거 안해도 자동으로 rowid만들긴 한다 
    title VARCHAR(100) NOT NULL,
    content VARCHAR(200) NOT NULL,
    creatdAt DATE NOT NULL
);

INSERT INTO articles
    (title, content, creatdAt)
VALUES
    ('제목', '내용', '2000-01-11');


SELECT * FROM articles;


INSERT INTO articles
    (title, content, creatdAt)
VALUES
    ('제목2', '내용2', '2000-01-11'),
    ('제목3', '내용3', '2000-01-11'),
    ('제목4', '내용4', '2000-01-11');


-- 위치인자처럼 모든 데이터 내용 적었을 때는 이렇게 해도 삽입이 된다.
-- 근데 AUTOINCREMENT했을 경우에는 안된다.COLUMN명 입력해줘야 삽입된다.
INSERT INTO articles
VALUES
    ('제목5', '내용5', '2000-01-11');


-- 테이블이 가진 모든 데이터가 삭제됨
DELETE FROM articles;

-- 5번 게시글만 삭제
DELETE FROM articles 
WHERE rowid = 5;

-- 1번 게시글만 삭제
DELETE FROM articles 
WHERE rowid = 1;


-- -- 이건 억지로 되겠지만
-- INSERT INTO articles
--     (rowid, title, content, creatdAt)
-- VALUES
--     (1, '제목1', '내용1', '2000-01-11')
-- -- 이건 안돼
-- INSERT INTO articles
--     (rowid, title, content, creatdAt)
-- VALUES
--     (2, '제목2', '내용2', '2000-01-11')



-- 1번 게시글의 제목을 '수정된 제목'
-- UPDATE 
UPDATE articles
SET title = '수정된 내용'
WHERE id = 1;


-- 2번 게시글의 제목을 '2번으로'
-- 2번 게시글의 내용을 '수정'
UPDATE articles
SET title = '2번으로',
    content = '수정'
WHERE id = 2;

SELECT * FROM articles;


-- * articles 테이블에서 작성일이
-- 오래된 순으로 레코드 2개 삭제

DELETE FROM articles
-- WHERE 절을 통해서 삭제 대상이 될 RECORD 찾기
-- WHERE 절에 작성한 내용을 통해 얻어진 데이터들을 삭제
-- id = 1 > id가 1인 데이터 하나 반환
-- 작성일이 오래된 데이터 2개를 찾아야 한다. 
    -- 작성일이 오래된 데이터 2개의 id 값을 찾기 
    -- SELECT로 찾기 
WHERE id IN (
    SELECT id FROM articles
    ORDER BY creatdAt LIMIT 2;
)

