CREATE TABLE example (
    LastName VARCHAR(50) NOT NULL,
    FirstName VARCHAR(50) NOT NULL
);

PRAGMA table_info('example');

ALTER TABLE
    example
ADD COLUMN
    Country VARCHAR(100) NOT NULL DEFAULT 0;

ALTER TABLE
    example
ADD COLUMN
    Age INTEGER NOT NULL;

ALTER TABLE
    example
ADD COLUMN
    Address VARCHAR(100) NOT NULL DEFAULT 0;



-- 컬럼 명 수정
-- Address -> PostCode
ALTER TABLE example RENAME COLUMN Address TO PostCode;


-- 컬럼 삭제하기 
ALTER TABLE example DROP COLUMN PostCode;

ALTER TABLE example RENAME TO new_examples;
DROP TABLE examples;

ALTER TABLE new_example RENAME TO examples;
DROP TABLE examples;