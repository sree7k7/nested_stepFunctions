# hello world lambda function

import os
import boto3
import json

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps('Hello from SUCCESS Lambda!')
    }