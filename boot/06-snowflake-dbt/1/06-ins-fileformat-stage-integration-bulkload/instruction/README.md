# Instruction

As your first task, Jane the HR has asked for your help. She would like you to help load some data into Snowflake.

- Files are stored in a private `S3` bucket.
- Files are in a delimited format, enclosed by double-quotes (") and delimited by pipes (|).
- Each file corresponds to a table.
- When adding new data in the future, new files will be put into the bucket.
- Jane doesn't mind if you manually load the data this time, but she would like you work towards automation in the future

## Concept
### Loading data
Snowflake supports loading data
- from
  - Local filesystem
  - Cloud storages
  - `Kafka` topics (via a connector)
- formatted as
  - delimited (`csv`, `tsv`, or in our case: `psv`)
  - semi-structured (`JSON`, `Arvo`, `ORC`, `Parquet`, `XML`)
- compressed as
  - `gizp`, `bzip2` etc.

Being a modern data warehouse, Snowflake has these configurable as objects.

### File Format
`FILE FORMAT` stores attributes to describe a file's format.

Some examples including field delimiter, record delimiter, has header or not and compression type.

[SQL reference]( https://docs.snowflake.com/en/sql-reference/sql/create-file-format.html)

### Stage
`STAGE` is essentially a location where Snowflake goes to find your files.
There are 2 types of `STAGE`:
- internal - a location within Snowflake manage storage, think of a personal folder
- external - a location in a Cloud storage external to Snowflake, e.g. `S3` buckets

A stage can handle both ingress and egress traffic.

[SQL reference](https://docs.snowflake.com/en/sql-reference/sql/create-stage.html)

### Storage Integration
`STAGE` can be used to specify a location in the Cloud. But it doesn't handle the identity and authentication needed to access that location.

`STORAGE INTEGRATION` is used for this purpose.

[SQL reference](https://docs.snowflake.com/en/sql-reference/sql/create-storage-integration.html)

### Copy Command
As simple as `COPY INTO ... FROM ...`

With `FILE FORMAT`, `STAGE` and `STORAGE INTEGRATION` created as objects, you can easily refer them in the `copy` command.

Note that the `COPY` command work both ways. You can `COPY` data into Snowflake and also `COPY` data out from Snowflake.

Extra stuff you can do with `COPY`
- light transformation
- `on_error` check

[SQL reference](https://docs.snowflake.com/en/sql-reference/sql/copy-into-table.html)


### Loading Data, Continuously
Wouldn't it be nice, if Snowflake can automatically run the `COPY` command when a new file is uploaded into a Cloud storage, say `S3`?

`Snowpipe` to the rescue!

`Snowpipe` builds upon the basic `COPY` command that we are going to demo. It has just a few extra configurations e.g. event notification. It is a good feature to use in your project.

[Guide](https://docs.snowflake.com/en/user-guide/data-load-snowpipe-auto-s3.html)

[SQL reference](https://docs.snowflake.com/en/sql-reference/sql/create-pipe.html)

## Task
Although many details are not clear to you yet, but now you understand it conceptually.

### High-level steps
In this demo, we will
- Upload data files into `S3`
- Create in AWS
  - `IAM` policy
  - `IAM` role: `snowflake_role`
- Create in Snowflake
  - `STORAGE INTEGRATION`: `S3_DECSYDLIU`
  - `FILE FORMAT`: `CSV_DECSYDLIU`
  - `STAGE`: `S3_HR_CSV`
- Run the `COPY` command to load one table for our HR

You will then, on your own
- Load the rest of the tables for HR (using role `HR_RW`)
- Load the salary table for payroll officer (using role `DBT_RW` manually for now)

### Steps on creating a `storage integration`
1. Create a non-public S3 bucket and upload all the files
2. Create an IAM policy (called `snowflake_access`) using JSON allowing both read and write on the whole bucket.
```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::<YOUR_BUCKET>",
            "Condition": {
                "StringLike": {
                    "s3:prefix": "*"
                }
            }
        },
        {
            "Effect": "Allow",
            "Action": [
                "s3:PutObject",
                "s3:GetObject",
                "s3:DeleteObjectVersion",
                "s3:DeleteObject",
                "s3:GetObjectVersion"
            ],
            "Resource": "arn:aws:s3:::<YOUR_BUCKET>/*"
        },
        {
            "Effect": "Allow",
            "Action": "s3:GetBucketLocation",
            "Resource": "arn:aws:s3:::<YOUR_BUCKET>"
        }
    ]
}
```
3. Create an IAM role (called `snowflake_role`)
   1. Trusted entity type: AWS account
   2. Trust "this account" for now
   3. Tick "Require external ID" and put in a dummy value 000 for now
   4. Assign the policy above
4. Note the ARN e.g. `arn:aws:iam::931718146526:role/snowflake_role`
5. `CREATE STORAGE INTEGRATION <YOUR_INTEGRATION>` using the role ARN
6. `DESC INTEGRATION <YOUR_INTEGRATION>` and note `STORAGE_AWS_IAM_USER_ARN` and `STORAGE_AWS_EXTERNAL_ID`
7. Edit Trusted Relationships of your role with the above 2 values

![](images/storage-integration-s3.png)