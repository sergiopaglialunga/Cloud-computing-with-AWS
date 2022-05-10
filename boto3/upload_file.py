import boto3

# Create an S3 client
s3 = boto3.client('s3')

filename = 'file.txt'
bucket_name = 'my-bucket'

# Upload a new file
data = open('test.jpg', 'rb')
s3.Bucket('my-bucket').put_object(Key='test.jpg', Body=data)

# using resource method
s3 = boto3.resource('s3')
s3.meta.client.upload_file('/tmp/hello.txt', 'mybucket', 'hello.txt')