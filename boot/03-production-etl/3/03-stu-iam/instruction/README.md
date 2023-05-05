# Instruction 

## Task 

We should avoid using the root account user unless it is for emergencies. The root account user has the ability to delete all users and resources in the AWS account. Therefore we should minimise use of the root accounts credentials to avoid issues. 

Create a new IAM user.

### Create user

1. Go to IAM 
2. Select "Users" 
3. Select "Add user" 
4. Provide a username (e.g. your first name and last name as one word)
5. Under "Select AWS credential type", tick both "Access key" and "Password" 
6. Provide a temporary password (store somewhere securely)
7. Click on "Next: permissions" 
8. Click on "Next: tags"
9. Click on "Next: review" 
10. Click on "Create user"

### Create policy 

1. Go to AWS IAM
2. Create a new policy to allow your user to view billing 

    ```json 
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "aws-portal:*",
                "Resource": "*"
            }
        ]
    }
    ```

3. Save the policy with the name "BillingFullAccess"

### Add policy to user 

1. Go to User 
2. Select "your_user" 
3. Select "Add permissions" 
4. Select "Attach existing policies directly" 
5. Select "BillingFullAccess" and "AdministratorAccess"
6. Select "Review"
7. Select "Add permissions"

