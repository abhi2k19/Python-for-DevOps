#--------------------List all Buckets Available---------------

import boto3

S3 = boto3.client('s3')
def s3_bucket_operations():
    try:
       response = S3.list_buckets()

       for bucket in response['Buckets']:
           print(bucket['Name'])
    except Exception as e:
        print(f"Error: {e}")
s3_bucket_operations()

#------------create s3 bucket------------------

import boto3
import logging
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region = None):
    try:
        if region is None: 
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket = bucket_name)
        else:
            s3_client = boto3.client('s3', region_name = region)
            location = {'LocationConstraint' : region}
            s3_client.create_bucket(Bucket = bucket_name, CreateBucketConfiguration=location)
    except ClientError as ce:
        logging.error(ce)
        return False
    return True
create_s3_bucket(bucket_name='mynewdemoboto30987r')

#------------create s3 bucket------------------

import boto3
import logging
from botocore.exceptions import ClientError

def create_s3_bucket(bucket_name, region=None):
    """
    Create an S3 bucket in the specified region.
    
    :param bucket_name: Name of the S3 bucket to create
    :param region: AWS region where the bucket will be created
    :return: True if bucket created successfully, False otherwise
    """
    try:
        # Initialize the S3 client
        if region is None or region == 'us-east-1': 
            # us-east-1 does not need CreateBucketConfiguration
            s3_client = boto3.client('s3')
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            # For other regions, include the CreateBucketConfiguration
            s3_client = boto3.client('s3', region_name=region)
            location = {'LocationConstraint': region}
            s3_client.create_bucket(Bucket=bucket_name, CreateBucketConfiguration=location)
    except ClientError as ce:
        logging.error(ce)
        return False
    return True

# Example usage
if __name__ == "__main__":
    logging.basicConfig(level=logging.ERROR)
    bucket_name = "mynewdemoboto30987r"  # Replace with a unique bucket name
    region = "us-east-1"  # Region (e.g., us-east-1, us-west-2, ap-south-1)
    if create_s3_bucket(bucket_name=bucket_name, region=region):
        print(f"Bucket '{bucket_name}' created successfully!")
    else:
        print(f"Failed to create bucket '{bucket_name}'.")
