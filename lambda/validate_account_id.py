import os
import boto3
import json

def lambda_handler(event, context):

    print("Received event: " + json.dumps(event, indent=2))
    print(len(event['accountId']))
    # Get the length of the account id
    accLen = len(event['accountId'])

    # Check if the account id is 12 digits

    if accLen == 12:
        print("Account id is valid")
        return {
            "statusCode": 200,
            # "body": json.dumps('Account id is valid')
        }
    else:
        print("Account id is invalid")
        return {
            "statusCode": 400,
            # "body": json.dumps('Account id is invalid')
        }

    