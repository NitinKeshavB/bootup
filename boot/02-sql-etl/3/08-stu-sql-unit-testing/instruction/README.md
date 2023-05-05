# SQL unit testing 

## Task

1. Create a unit test to test `test_extract_load_incremental()`
    - To test our extract and load pipeline, we will need to generate mock data which we can seed into our source database
    - We will also need to generate a mock SQL extract file 
    - Then we will run the pipeline and validate that the data loaded into the target database matches our mock data
    - We will also need to cleanup the mock data from (1) source database and (2) target database (3) the mock SQL extract file in our directory 

Note: We would typically run unit tests in a non-production database to avoid dropping or deleting any production data. Therefore, you should not be concerned that you are executing drop table statements in your unit tests. The caveat is that you shouldn't run unit tests on a production database. 

