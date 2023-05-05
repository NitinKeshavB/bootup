# Instruction

## Task

This exercise costs about 1 dollar.

1. create a new s3 bucket with versioning enabled
2. upload dags files in to dag folder, upload requirements.txt
3. use MWAA 2.2.2
4. set s3 bucket, dag folder, requirements
5. create mwaa vpc (which goes to cloudformation, use all default values)
6. refresh and select the created vpc, use it's private subnets
7. webserver - public network
8. tick create new security group
9. small size, maximum worker count = 1
10. execution role - let AWS create new role
11. run an example DAG and check logs

Clean Up:
1. Delete the MWAA environment
2. Delete the MWAA security group
3. In CloudFormation, delete the CloudFormation Stack
4. Delete the files in S3