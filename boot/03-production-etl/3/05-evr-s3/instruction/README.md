# Instruction 

## Task 


### Create bucket 

1. Go to AWS console 
2. Search for "S3" 
3. Select "Create bucket": 
    - Bucket name: `<provide_a_name>`
    - AWS Region: `<choose_a_local_region>`
    - [x] ACLs disabled (recommended) 
    - [ ] Block all public access 
    - [x] I acknowledge that the current settings might result in this bucket and the objects within becoming public.
    - Select "Create bucket"

### Configure bucket policy 

1. Select newly created bucket 
2. Select "Permissions"
3. Bucket policy > Edit: 

    ```json
    {
	"Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicRead",
                "Effect": "Allow",
                "Principal": "*",
                "Action": [
                    "s3:GetObject",
                    "s3:GetObjectVersion"
                ],
                "Resource": "arn:aws:s3:::your_bucket_name/*"
            }
        ]
    }
    ```    
    Note: This policy will allow any one to download objects in the bucket. 

4. Select "Save changes" 


### Upload and download object 

1. Upload `hello_world.txt` to the bucket 
2. Click on the uploaded file 
3. Copy the object URL and paste in a new browser window. You should see the contents of the file displayed in the browser or downloaded. 

