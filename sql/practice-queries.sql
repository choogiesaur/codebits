-- Select first name of patients whose first name starts with 'C'

SELECT first_name
from patients
where SUBSTRING(first_name, 1, 1) == 'C'

-- OR, with regex:

SELECT first_name
from patients
where first_name LIKE 'C%'
