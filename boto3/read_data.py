import boto3

# Creating a bucket in AWS S3
def create_bucket(bucket_name)
    client.create_bucket(Bucket='eng110-sergio')

# Create the S3 object
obj = client.get_object(
    Bucket = 'eng110-sergio',
    Key = 'test.csv'
)
    
# Read data from the S3 object
data = pandas.read_csv(obj['Body'])
    
# Print the data frame
print('Printing the data frame...')
print(data)

# Create an S3 client
s3 = boto3.client('s3')

filename = 'file.txt'
bucket_name = 'my-bucket'
