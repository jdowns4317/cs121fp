-- CS 121 Final Project
-- James Downs (jdowns@caltech.edu), Thorsen Kristufek (tkristuf@caltech.edu)
-- Setup file for our higher education database.
-- Our application will have information about colleges and universities
-- so that prospective college students can easily find institutions that meet
-- their desired criteria. Colleges will also be able to interact with the
-- database to keep their information updated.

-- setup database:
DROP DATABASE IF EXISTS finaldb;
CREATE DATABASE finaldb;
USE finaldb;

-- clean up old tables
DROP TABLE IF EXISTS cost;
DROP TABLE IF EXISTS sports_programs;
DROP TABLE IF EXISTS sports_grad_rate;
DROP TABLE IF EXISTS city_pop;
DROP TABLE IF EXISTS basic_college_info;

-- Table representing the basic information about each college in the USA
-- Each college is uniquely identified by the 
-- u_id (Department of Education's unit id)
-- The population may be null (missing), but the rest of the traits cannot be
CREATE TABLE basic_college_info (
    u_id            INT PRIMARY KEY,
    college_name    VARCHAR(100) NOT NULL,
    -- total undergrad enrollment
    ug_pop          INT,
    -- Campus location city
    city            VARCHAR(25) NOT NULL,
    -- Campus state (abbreviation)
    state_abbr      CHAR(2) NOT NULL,
    -- Binary HBCU Flag
    hbcu            TINYINT DEFAULT NULL,
    -- Binary Men Only Flag
    men_only        TINYINT DEFAULT NULL,
    -- Binary Women Only Flag
    women_only      TINYINT DEFAULT NULL,
    -- Highest degree awarded (0: Non-degree-granting, 1 Certificate degree,
    -- 2: Associate degree, 3: Bachelor's degree, 4: Graduate degree)
    highest_degree  TINYINT,
    -- Admission rate
    admission_rate  DECIMAL(6, 5) DEFAULT NULL,
    -- College mission (to be provided by administrators)
    mission         VARCHAR(500) DEFAULT NULL,

    -- Ensure the flags are binary
    CHECK (hbcu IN (0, 1)),
    CHECK (men_only IN (0, 1)),
    CHECK (women_only IN (0, 1))
);

-- Table representing the cost of attending colleges
-- Represented seperately to allow further functionality for many types of
-- prices such as in-district, on-scholarship, etc.
-- These prices could simply be distinguished by adding more flags.
-- No entries may be null
CREATE TABLE cost (
    -- p_id of the price entry
    p_id    INTEGER AUTO_INCREMENT,
    -- u_id of the corresponding university
    u_id    INT,
    -- Cost of tuition
    tuition INT,
    -- Binary in-state flag
    in_state TINYINT NOT NULL,

    PRIMARY KEY (p_id),
    -- Ensure the in_state flag is binary
    CHECK (in_state IN (0,1))
);

-- Table representing the athletic programs offered by colleges
-- Currently restricted to football, basketball, baseball, and
-- cross country/track
CREATE TABLE sports_programs (
    u_id    INT,
    -- National Athletic Association
    assoc   VARCHAR(5),
    -- sport abbreviation
    sport   CHAR(3) NOT NULL,

    -- multivalued because there could be multiple programs per school
    -- but each school/sport combo is unique
    PRIMARY KEY (u_id, sport),

    FOREIGN KEY (u_id) REFERENCES basic_college_info(u_id)
        ON DELETE CASCADE
);

-- Table representing the graduation rate corresponding to the D1
-- version of each sport 
CREATE TABLE sports_grad_rate (
    sport          CHAR(3) PRIMARY KEY,
    -- Federal Graduation Rate (percentage) within 6 years of enrollment
    fed_grad_rate  INT NOT NULL
);

-- Table containing the population of cities colleges are located in
CREATE TABLE city_pop (
    city            VARCHAR(50) NOT NULL,
    -- state abbreviation
    state_abbr      CHAR(2) NOT NULL,
    population      INT,

    PRIMARY KEY (city, state_abbr)
);

CREATE INDEX idx_name ON basic_college_info(college_name);