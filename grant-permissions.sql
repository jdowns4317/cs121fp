-- CS 121 Final Project
-- James Downs (jdowns@caltech.edu), Thorsen Kristufek (tkristuf@caltech.edu)
-- Setup client and admin MySQL users with different privilages.
-- Clients can select, admins have complete control to select, update, insert,
-- and delete

-- clean up existing users:
DROP USER IF EXISTS 'eduadmin'@'localhost';
DROP USER IF EXISTS 'educlient'@'localhost';

CREATE USER 'eduadmin'@'localhost' IDENTIFIED BY 'adminpw';
CREATE USER 'educlient'@'localhost' IDENTIFIED BY 'clientpw';

-- Allow the administrators complete control to view, update, insert new, or
-- remove data. Further, more complicated security checks such as ensuring
-- they are only modifiying information for the college they work for,
-- could be added in the future.
GRANT ALL PRIVILEGES on *.* TO 'eduadmin'@'localhost';

-- Let the student/parent clients view the education data
GRANT SELECT ON finaldb.* TO 'educlient'@'localhost';
GRANT EXECUTE ON finaldb.* TO 'educlient'@'localhost';

-- update the privileges.
FLUSH PRIVILEGES;
