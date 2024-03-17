-- Thorsen Kristufek and James Downs


-- RA 1 query
-- Computes the average tuition cost of non-HBCU colleges grouped by state.
SELECT b.state_abbr, AVG(c.tuition) AS avg_tuition
FROM basic_college_info b
JOIN cost c ON b.u_id = c.u_id
WHERE b.hbcu = 0
GROUP BY b.state_abbr;

-- RA 2 query
-- Finds colleges located in cities with populations greater than 100,000.
SELECT b.college_name, b.city, b.state_abbr, cp.population
FROM basic_college_info b
JOIN city_pop cp ON b.city = cp.city AND b.state_abbr = cp.state_abbr
WHERE cp.population > 100000;

-- RA 3 query
-- Retrieves colleges that offer both football and basketball programs.
SELECT DISTINCT b.u_id, b.college_name
FROM basic_college_info b
JOIN sports_programs sp1 ON b.u_id = sp1.u_id AND sp1.sport = 'MFB'
JOIN sports_programs sp2 ON b.u_id = sp2.u_id AND sp2.sport = 'MBB';

-- Low admin
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE admission_rate IS NOT NULL AND admission_rate <> 0
ORDER BY admission_rate
LIMIT 10;

--Outputs Men's only colleges
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE men_only = 1
ORDER BY college_name;

--Outputs women's only colleges
SELECT college_name, ug_pop, admission_rate, city, state_abbr
FROM basic_college_info
WHERE women_only = 1
ORDER BY college_name;

--Colleges with Sports programs in a user
--input Acceptance Rate range
SELECT college_name, ug_pop, admission_rate, city, state_abbr, count_sports(u_id)
FROM basic_college_info
WHERE count_sports(u_id) > 0 AND admission_rate BETWEEN 0.5 AND 0.55
ORDER BY college_name;

--Colleges within pop range given
SELECT b.college_name, b.ug_pop, b.admission_rate, b.city, b.state_abbr, 
c.population
FROM basic_college_info b
JOIN city_pop c ON b.city = c.city AND b.state_abbr = c.state_abbr
WHERE c.population BETWEEN 1000 AND 2000
ORDER BY c.population;

-- Outputs detailed sports info
-- about a user input college

SELECT sp.sport, sgr.fed_grad_rate
FROM sports_programs sp
JOIN basic_college_info bci ON sp.u_id = bci.u_id
JOIN sports_grad_rate sgr ON sp.sport = sgr.sport
WHERE bci.college_name = 'California Institute of Technology';