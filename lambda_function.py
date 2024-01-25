import boto3
def lambda_handler(event, context):
    result = "25 Jan 24, 8:20pm cooling weather. Annyeonghaseyo Jinn Liong Nim. "
    return {
        'statusCode' : 200,
        'body': result
    }