import json
import urllib.parse
import boto3
import csv
from io import StringIO
from app import transform

s3 = boto3.client('s3')

def lambda_handler(event, context):
    # Extract bucket and key from the S3 event
    source_bucket = event['Records'][0]['s3']['bucket']['name']
    key = urllib.parse.unquote_plus(event['Records'][0]['s3']['object']['key'], encoding='utf-8')

    # Retrieve S3 object content
    s3_resource = boto3.resource('s3')
    s3_object = s3_resource.Object(source_bucket, key)
    data = s3_object.get()['Body'].read().decode('utf-8').splitlines()

    # Define CSV headers
    headers = ['date', 'location', 'name', 'order', 'total_price', 'payment_type', 'card_no']

    # Process CSV data
    list_of_dict = []
    csv_reader = csv.reader(data)
    
    for line in csv_reader:
        zipped_data = zip(headers, line)
        row_dict = dict(zipped_data)
        list_of_dict.append(row_dict)

    transformed_data = transform(list_of_dict)
    
    # Convert the modified data back to CSV
    csv_buffer = StringIO()
    csv_writer = csv.DictWriter(csv_buffer, fieldnames=headers)
    csv_writer.writeheader()
    csv_writer.writerows(transformed_data)
    modified_file_content = csv_buffer.getvalue()

    # Write the modified file to the new bucket
    destination_bucket = '2muchsauce-cleandata'
    s3.put_object(Body=modified_file_content, Bucket=destination_bucket, Key=key)

    return {
        'statusCode': 200,
        'body': f'File {key} copied from {source_bucket} and cleaned to {destination_bucket} with modifications'
    }
