import boto3
import json

def lambda_handler(event, context):
    try:
        bucket_name = event['body']['bucket']

        s3 = boto3.client('s3')
        s3.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': 'us-east-1'}
        )

        return {
            'statusCode': 200,
            'body': json.dumps(f"Bucket '{bucket_name}' creado exitosamente")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
