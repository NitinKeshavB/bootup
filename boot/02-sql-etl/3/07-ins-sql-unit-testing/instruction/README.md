# SQL unit testing 

## Concept 

**Q: What are the top 3 main types of testing for data engineering?**

**Q: What are the 3 steps when writing a unit test? (Hint: AAA)**

## Implement 

Let's now take a look at how we can implement unit tests for SQL ELT scripts. 

1. `test_extract_load()`
    - To test our extract and load pipeline, we will need to generate mock data which we can seed into our source database
    - We will also need to generate a mock SQL extract file 
    - Then we will run the pipeline and validate that the data loaded into the target database matches our mock data
    - We will also need to cleanup the mock data from (1) source database and (2) target database (3) the mock SQL extract file in our directory 
2. `test_transform()`
    - To test our transformations, the unit test can be complicated to write as we will need to generate mock data for every table we are querying from in our select statement
    - The steps are similar to `test_extract_load()`, with the exception of one additional step, and that is to generate an expected dataframe. The expected dataframe is what we will use to validate that the transformation was performed correctly. 
    - We must make sure to perform the cleanup as well and not leave any traces behind. 

Note: We would typically run unit tests in a non-production database to avoid dropping or deleting any production data. Therefore, you should not be concerned that you are executing drop table statements in your unit tests. The caveat is that you shouldn't run unit tests on a production database. 

