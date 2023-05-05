-- continue the task to load data for hr and payroll

-------------------------------------------------------
-- when creating tables, use these data type: timestamp, varchar, bigint

-------------------------------------------------------
-- load employees
-- table name: HR.SOURCE.EMPLOYEES

-- 1. create table
<YOUR CODE HERE>

-- 2. copy
<YOUR CODE HERE>

-------------------------------------------------------
-- load titles
-- table name: HR.SOURCE.TITLES

-- 1. create table
<YOUR CODE HERE>

-- 2. copy
<YOUR CODE HERE>

-------------------------------------------------------
-- create file format object in hr.util for the json type
-- file format name: JSON_DECSYDLIU
USE ROLE HR_RW;
USE HR.UTIL;
USE WAREHOUSE ETL;
<YOUR CODE HERE>

-------------------------------------------------------
-- create stage in hr.util
-- stage name: S3_HR_JSON
<YOUR CODE HERE>

-------------------------------------------------------
-- load dept_manager (you'll see one json object per role, we'll see how to use it next)
-- 1. create
CREATE OR REPLACE TABLE HR.SOURCE.DEPT_MANAGER
 (raw_obj variant
 );

-- 2. copy
 <YOUR CODE HERE>

-------------------------------------------------------
USE ROLE SECURITYADMIN;
GRANT CREATE FILE FORMAT ON SCHEMA PAYROLL.UTIL TO ROLE DBT_RW;

USE ROLE DBT_RW;
USE PAYROLL.UTIL;
USE WAREHOUSE ETL;

-- create file format in payroll.util
-- file format name: CSV_DECSYDLIU
CREATE OR REPLACE FILE FORMAT CSV_DECSYDLIU
    TYPE = CSV
    RECORD_DELIMITER = '\n'
    FIELD_DELIMITER = '|'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1;

-- observe the same name CSV_DECSYDLIU in hr and payroll database, it is schema level object, not account level
USE ROLE ACCOUNTADMIN;
USE PAYROLL.UTIL;
SHOW FILE FORMATS;
USE HR.UTIL;
SHOW FILE FORMATS;

-------------------------------------------------------
USE ROLE SECURITYADMIN;
GRANT CREATE STAGE ON SCHEMA PAYROLL.UTIL TO ROLE DBT_RW;
GRANT USAGE ON INTEGRATION S3_DECSYDLIU TO ROLE DBT_RW;

USE ROLE DBT_RW;
USE WAREHOUSE ETL;
USE SCHEMA PAYROLL.UTIL;

-- create stage in payroll.util
-- stage name: S3_PAYROLL_CSV
<YOUR CODE HERE>

-------------------------------------------------------
-- load salaries
-- table name: PAYROLL.SOURCE.SALARIES

-- 1. create
<YOUR CODE HERE>

-- 2. copy
<YOUR CODE HERE>