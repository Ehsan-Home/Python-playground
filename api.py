import json

def handleTestAPI(event, context):
    #1 parse query string params
    transactionId = event['queryStringParameters']['transactionId']
    transactionType = event['queryStringParameters']['type']
    transactionAmount = event['queryStringParameters']['amount']

    print("transaction id " + transactionId)
    print("transaction type " + transactionType)
    print("transaction amount " + transactionAmount)

    #2 Construct the body of the response obj
    transactionResponse = {}
    transactionResponse['transactionId'] = transactionId
    transactionResponse['type'] = transactionType
    transactionResponse['amount'] = transactionAmount
    transactionResponse['message'] = "Hello from lambda Ehsan Ghasaei"

    #Construct a HTTP response obj
    responseObj = {}
    responseObj['statusCode'] = 200
    responseObj['headers'] = {}
    responseObj['headers']['Content-Type'] = "application/json"
    responseObj['body'] = json.dumps(transactionResponse)

    # Return response obj
    return responseObj
