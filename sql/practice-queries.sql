-- Select first name of patients whose first name starts with 'C'

SELECT first_name
from patients
where SUBSTRING(first_name, 1, 1) == 'C';

-- OR, with regex:

SELECT first_name
from patients
where first_name LIKE 'C%';

-- Weight in a range 100-120 inclusive:

SELECT first_name, last_name
from patients
where weight >= 100 and weight <= 120;

-- OR, with BETWEEN operator

SELECT first_name, last_name
FROM patients
WHERE weight BETWEEN 100 AND 120;


-- UPDATE statement
UPDATE patients
SET allergies='NKA'
WHERE allergies IS NULL

-- Aggregations: COUNT
-- count() with distinct + field, counts distinct values of the given field
select count(distinct sID) 
from Apply 
where cName = 'Cornell';

-- Colleges with < 5 distinct APPLICANTS
select cName 
from Apply 
group by cName 
having count(distinct sID) < 5;

-- vs ...

-- Colleges with < 5 APPLICATIONS
select cName 
from Apply 
group by cName 
having count(*) < 5; -- each row is an application
