import boto3
import base64
import json

def lambda_handler(event, context):
    try:
        # Si event['body'] es string (como ocurre normalmente), lo decodificamos
        body = event['body']
        if isinstance(body, str):
            body = json.loads(body)

        bucket_name = body['bucket']
        file_name = body['file_name']
        file_content_base64 = body['file_content']

        # Decodificamos el contenido del archivo
        file_content = base64.b64decode(file_content_base64)

        # Subimos el archivo a S3
        s3 = boto3.client('s3')
        s3.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)

        return {
            'statusCode': 200,
            'body': json.dumps(f"Archivo '{file_name}' subido exitosamente al bucket '{bucket_name}'")
        }

    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({'error': str(e)})
        }
