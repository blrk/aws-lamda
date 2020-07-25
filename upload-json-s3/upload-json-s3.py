import json
import boto3

s3 = boto3.client('s3')

def lambda_handler(event, context):
	bucket ='awslamdatrigger'
    
    transactionToUpload = {}
	transactionToUpload['transactionId'] = '12345'
	transactionToUpload['type'] = 'PAYMENT'
	transactionToUpload['amount'] = 20
	transactionToUpload['studentId'] = 'UR18CS001'

	fileName = 'UR18CS001' + '.json'

	uploadByteStream = bytes(json.dumps(transactionToUpload).encode('UTF-8'))

	s3.put_object(Bucket=bucket, Key=fileName, Body=uploadByteStream)

	print('Put Complete')
