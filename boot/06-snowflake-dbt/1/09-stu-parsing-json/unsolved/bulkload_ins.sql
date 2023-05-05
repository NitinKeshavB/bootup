-- cheat code for convenience
USE ROLE SECURITYADMIN;
GRANT ROLE DBT_RW TO ROLE ACCOUNTADMIN;
GRANT ROLE HR_RW TO USER ACCOUNTADMIN;
GRANT ROLE PAYROLL_R TO USER ACCOUNTADMIN;

-- create file format in hr.util
USE ROLE SECURITYADMIN;
GRANT CREATE FILE FORMAT ON SCHEMA HR.UTIL TO ROLE HR_RW;

USE ROLE HR_RW;
USE HR.UTIL;
USE WAREHOUSE ETL;
CREATE OR REPLACE FILE FORMAT CSV_DECSYDLIU
    TYPE = CSV
    RECORD_DELIMITER = '\n'
    FIELD_DELIMITER = '|'
    FIELD_OPTIONALLY_ENCLOSED_BY = '"'
    SKIP_HEADER = 1;

SHOW FILE FORMATS;

-- create storage integration (account level)
USE ROLE ACCOUNTADMIN;
CREATE OR REPLACE STORAGE INTEGRATION S3_DECSYDLIU
  TYPE = EXTERNAL_STAGE
  STORAGE_PROVIDER = S3
  ENABLED = TRUE
  STORAGE_AWS_ROLE_ARN = 'arn:aws:iam::931718146526:role/snowflake_role'
  STORAGE_ALLOWED_LOCATIONS = ('s3://decsydliu/');

SHOW INTEGRATIONS;
DESCRIBE INTEGRATION S3_DECSYDLIU;

-- create stage in hr.util
USE ROLE SECURITYADMIN;
GRANT CREATE STAGE ON SCHEMA HR.UTIL TO ROLE HR_RW;
GRANT USAGE ON INTEGRATION S3_DECSYDLIU TO ROLE HR_RW;

USE ROLE HR_RW;
USE WAREHOUSE ETL;
USE SCHEMA HR.UTIL;

CREATE OR REPLACE STAGE S3_HR_CSV
  STORAGE_INTEGRATION = S3_DECSYDLIU
  URL = 's3://decsydliu/hr/'
  FILE_FORMAT = HR.UTIL.CSV_DECSYDLIU;

LIST @HR.UTIL.S3_HR_CSV;

-- copy data
CREATE OR REPLACE TABLE HR.SOURCE.DEPT_EMP
 (emp_no varchar,
 dept_no varchar,
 from_date timestamp,
 to_date timestamp
 );


COPY INTO HR.SOURCE.DEPT_EMP
  FROM @HR.UTIL.S3_HR_CSV/dept_emp.csv;

-- check
SELECT * FROM HR.SOURCE.DEPT_EMP LIMIT 10;