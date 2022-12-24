
-- create
CREATE TABLE EMPLOYEE (
  empId INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO EMPLOYEE VALUES (0001, 'Иван', 18, 'ул Пушкина д. 15');
INSERT INTO EMPLOYEE VALUES (0002, 'Петр', 22, 'Невский пр, д. 1');
INSERT INTO EMPLOYEE VALUES (0003, 'Анна', 26, 'канал Грибоедова, д. 11');
INSERT INTO EMPLOYEE VALUES (0004, 'Юлия', 15, 'ул. Рубинштейна, д. 24');
INSERT INTO EMPLOYEE VALUES (0005, 'Боб', 28, 'Литейный пр, д. 1');
INSERT INTO EMPLOYEE VALUES (0006, 'Сергей', 36, 'ул. Садовая, д. 19');

-- fetch 
SELECT * FROM EMPLOYEE;
