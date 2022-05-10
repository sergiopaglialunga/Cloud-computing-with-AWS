import boto3

AWS_REGION = "eu-west-1"

# instantiate the Boto3 S3 client
client = boto3.client("s3", region_name=AWS_REGION)

bucket_name = "hands-on-cloud-demo-bucket"
location = {'LocationConstraint': AWS_REGION}

response = client.create_bucket(Bucket='eng110-sergio')

    