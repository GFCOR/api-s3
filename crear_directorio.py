import boto3
import json

def lambda_handler(event, context):
    try:
        bucket_name = event['body']['bucket']
        directorio = event['body']['directorio'].strip('/') + '/'

        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=directorio)

        return {
            'statusCode': 200,
            'body': json.dumps(f"Directorio '{directorio}' creado exitosamente en bucket '{bucket_name}'")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
