import json
from helper.dummy import hello

def lambda_handler(event, context):
    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": hello()
        }),
    }
