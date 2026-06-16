import json
import boto3

client = boto3.client('stepfunctions')

STEP_FUNCTION_ARN = "arn:aws:states:ap-south-1:989571800635:stateMachine:ecommerce-etl-project"

def lambda_handler(event, context):

    print("✅ S3 event received:", json.dumps(event))

    response = client.start_execution(
        stateMachineArn=STEP_FUNCTION_ARN,
        input=json.dumps(event)
    )

    print("✅ Step Function triggered:", response)

    return {
        "statusCode": 200
    }