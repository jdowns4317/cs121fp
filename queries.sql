-- Thorsen Kristufek and James Downs


-- RA 1 query
-- Computes the average tuition cost of non-HBCU colleges grouped by state.
SELECT b.state_abbr, AVG(c.tuition) AS avg_tuition
FROM basic_college_info b
JOIN cost c ON b.u_id = c.u_id
WHERE b.hbcu = 0
GROUP BY b.state_abbr;

-- RA 2 query!
-- Finds colleges located in cities with populations greater than 100,000.
SELECT b.college_name, b.city, b.state_abbr, cp.population
FROM basic_college_info b
JOIN city_pop cp ON b.city = cp.city AND b.state_abbr = cp.state_abbr
WHERE cp.population > 100000;

-- RA 3 query
-- Retrieves colleges that offer both football and basketball programs.
SELECT DISTINCT b.u_id, b.college_name
FROM basic_college_info b
JOIN sports_programs sp1 ON b.u_id = sp1.u_id AND sp1.sport = 'FB'
JOIN sports_programs sp2 ON b.u_id = sp2.u_id AND sp2.sport = 'BB';
