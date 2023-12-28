import boto3
#botocore module is for exception handling

client = boto3.client('s3')

response = client.get_bucket_acl(
    Bucket='boto3-bucket-baig',

)

print(response)
print(type(response))

owner_info = response.get('Owner', {})

print(owner_info)