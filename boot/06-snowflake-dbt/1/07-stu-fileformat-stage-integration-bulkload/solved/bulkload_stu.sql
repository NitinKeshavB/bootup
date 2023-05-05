-------------------------------------------------------
-- load employees
CREATE OR REPLACE TABLE HR.SOURCE.EMPLOYEES
 (emp_no varchar,
 birth_date timestamp,
 first_name varchar,
 last_name varchar,
 gender varchar,
 hire_date timestamp,
 updated_at timestamp
 );

COPY INTO HR.SOURCE.EMPLOYEES
  FROM @HR.UTIL.S3_HR_CSV/employees.csv;

-- check
SELECT * FROM HR.SOURCE.EMPLOYEES LIMIT 10;

-------------------------------------------------------
-- load titles
CREATE OR REPLACE TABLE HR.SOURCE.TITLES
 (emp_no varchar,
 title varchar,
 from_date timestamp,
 to_date timestamp
 );

COPY INTO HR.SOURCE.TITLES
  FROM @HR.UTIL.S3_HR_CSV/titles.csv;

-- check
SELECT * FROM HR.SOURCE.TITLES LIMIT 10;

-------------------------------------------------------
-- create file format in hr.util
USE ROLE HR_RW;
USE HR.UTIL;
USE WAREHOUSE ETL;
CREATE OR REPLACE FILE FORMAT JSON_DECSYDLIU
    TYPE = JSON;

SHOW FILE FORMATS;

-- create stage in hr.util
CREATE OR REPLACE STAGE S3_HR_JSON
  STORAGE_INTEGRATION = S3_DECSYDLIU
  URL = 's3://decsydliu/hr/'
  FILE_FORMAT = HR.UTIL.JSON_DECSYDLIU;

LIST @HR.UTIL.S3_HR_JSON;

-- load dept_manager
CREATE OR REPLACE TABLE HR.SOURCE.DEPT_MANAGER
 (raw_obj variant
 );

COPY INTO HR.SOURCE.DEPT_MANAGER
  FROM @HR.UTIL.S3_HR_JSON/dept_manager.json;

-- check
SELECT * FROM HR.SOURCE.DEPT_MANAGER LIMIT 10;
-------------------------------------------------------

-- create file format in payroll.util
USE ROLE SECURITYADMIN;
GRANT CREATE FILE FORMAT ON SCHEMA PAYROLL.UTIL TO ROLE DBT_RW;

USE ROLE DBT_RW;
USE PAYROLL.UTIL;
USE WAREHOUSE ETL;
CREATE OR REPLACE FILE FORMAT CSV_DECSYDLIU
    TYPE = CSV
    RECORD_DELIMITER = '\n'
    FIELD_DELIMITER = '|'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1;

SHOW FILE FORMATS;

-- create stage in payroll.util
USE ROLE SECURITYADMIN;
GRANT CREATE STAGE ON SCHEMA PAYROLL.UTIL TO ROLE DBT_RW;
GRANT USAGE ON INTEGRATION S3_DECSYDLIU TO ROLE DBT_RW;

USE ROLE DBT_RW;
USE WAREHOUSE ETL;
USE SCHEMA PAYROLL.UTIL;

CREATE OR REPLACE STAGE S3_PAYROLL_CSV
  STORAGE_INTEGRATION = S3_DECSYDLIU
  URL = 's3://decsydliu/payroll/'
  FILE_FORMAT = PAYROLL.UTIL.CSV_DECSYDLIU;

LIST @PAYROLL.UTIL.S3_PAYROLL_CSV;

-- copy data
CREATE OR REPLACE TABLE PAYROLL.SOURCE.SALARIES
 (emp_no varchar,
 salary bigint,
 from_date timestamp,
 to_date timestamp
 );


COPY INTO PAYROLL.SOURCE.SALARIES
  FROM @PAYROLL.UTIL.S3_PAYROLL_CSV/salaries.csv;

-- check
SELECT * FROM PAYROLL.SOURCE.SALARIES LIMIT 10;
