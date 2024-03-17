-- CS 121 Final Project
-- James Downs (jdowns@caltech.edu), Thorsen Kristufek (tkristuf@caltech.edu)
-- Setup file for the routines used by our higher education database
-- application.

-- Cleanup
DROP FUNCTION IF EXISTS count_sports;
DROP PROCEDURE IF EXISTS update_admission_rate;
DROP TRIGGER IF EXISTS check_flags;

-- Counts the number of sports a school offers
DELIMITER !
CREATE FUNCTION count_sports(u_id INT) RETURNS INT DETERMINISTIC
BEGIN
    DECLARE sport_count INT;
    SELECT COUNT(*) INTO sport_count FROM sports_programs sp 
        WHERE sp.u_id = u_id;
    RETURN sport_count;
END !
DELIMITER ;

-- Procedure for admins to update the information about their school
DELIMITER !
CREATE PROCEDURE update_all_info(new_u_id INT, 
                                new_ug_pop INT,
                                new_hbcu TINYINT,
                                new_men_only TINYINT,
                                new_women_only TINYINT,
                                new_highest_degree TINYINT,
                                new_admission_rate DECIMAL(6,5))
BEGIN 
    UPDATE basic_college_info 
    SET ug_pop = new_ug_pop, hbcu = new_hbcu, men_only = new_men_only,
        women_only = new_women_only, highest_degree = new_highest_degree,
        admission_rate = new_admission_rate
    WHERE basic_college_info.u_id = new_u_id;
END !
DELIMITER ;

-- Trigger to ensure that both of the men_only and women_only flags aren't
-- set to true at the same time. If they are, they will be updated to both be
-- false.
DELIMITER !
CREATE TRIGGER check_flags
AFTER UPDATE ON basic_college_info
FOR EACH ROW
BEGIN
    IF NEW.men_only = 1 AND NEW.women_only = 1 THEN
        UPDATE basic_college_info
        SET men_only = 0, women_only = 0
        WHERE u_id = NEW.u_id;
    END IF;
END !
DELIMITER ;

