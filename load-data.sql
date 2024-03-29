-- CS 121 Final Project
-- James Downs (jdowns@caltech.edu), Thorsen Kristufek (tkristuf@caltech.edu)
-- Loads data from the relevant csv files into the tables specified by
-- setup.sql.

-- basic_college_info table data
LOAD DATA LOCAL INFILE 'processed_data/basic_info.csv' 
INTO TABLE basic_college_info 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(u_id, college_name, ug_pop, city, state_abbr, hbcu, men_only, women_only, 
highest_degree, admission_rate);

-- cost table data
LOAD DATA LOCAL INFILE 'processed_data/cost.csv' 
INTO TABLE cost 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS
(u_id, tuition, in_state);

-- sports_programs table data
LOAD DATA LOCAL INFILE 'processed_data/sport_programs.csv' 
INTO TABLE sports_programs 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- sports_grad_rate table data
LOAD DATA LOCAL INFILE 'processed_data/sport_grad.csv' 
INTO TABLE sports_grad_rate 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;

-- city_pop table data
LOAD DATA LOCAL INFILE 'processed_data/population.csv' 
INTO TABLE city_pop  
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"'
LINES TERMINATED BY '\n'
IGNORE 1 ROWS;
