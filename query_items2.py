import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = dynamodb.Table('cbw-test-table')

resp = table.query(KeyConditionExpression=Key('user-id').eq('a105000'))
print(resp)
print("The query returned the following items:")
for item in resp['Items']:
    print(item)
