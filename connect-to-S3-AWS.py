import json
import boto3


def lambda_handler(event,context):
    print("event: ", event)
    print("context: ", context)
    #1 Get the bucket name
    bucketName = event['Records'][0]['s3']['bucket']['name']

    #2 Get the file/key name
    key = event['Records'][0]['s3']['object']['key']

    try:
        #3 Fetch the file from S3
        response = boto3.client("s3").get_object(Bucket=bucketName, Key=key)

        #4 Deserialize the file's content
        text = response["Body"].read().decode()
        data = json.loads(text)

        #5 print data
        print("data:",data)

        transaction = data['transactions'] 
        for record in transaction:
            print(record['transType'])
        return "Success!"

    except Exception as e:
        print(e)
        raise e