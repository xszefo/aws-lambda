import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
    my_bucket = s3.list_objects(Bucket='psum-s3-bucket')
    
    for s3_file in my_bucket['Contents']:
        print(s3_file['Key'])
        
    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
