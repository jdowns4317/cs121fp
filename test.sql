SELECT college_name AS "College Name", ug_pop AS "Undergraduate Population",
admission_rate AS "Admission Rate", 
city AS City, state_abbr AS "STATE Abbreviation"
FROM basic_college_info
WHERE admission_rate IS NOT NULL
ORDER BY admission_rate ASC
LIMIT 10; 

SELECT college_name, ug_pop, admission_rate, city, state_abbr, count_sports(u_id)
FROM basic_college_info
WHERE count_sports(u_id) > 0 AND admission_rate BETWEEN 0.5 AND 0.6
ORDER BY college_name;

SELECT sp.sport, sgr.fed_grad_rate
FROM sports_programs sp
JOIN basic_college_info bci ON sp.u_id = bci.u_id
JOIN sports_grad_rate sgr ON sp.sport = sgr.sport
WHERE bci.college_name = 'California Institute of Technology';

UPDATE basic_college_info
SET mission = 'try'
WHERE u_id = 110413;

UPDATE basic_college_info
SET admission_rate = 0.5
WHERE u_id = 110413;