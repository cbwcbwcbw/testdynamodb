import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = dynamodb.Table('cbw-test-table')

id=80000
while True:
    userid="a"+str(id)
    resp = table.query(KeyConditionExpression=Key('user-id').eq(userid))
    if resp['Items'] :
        id += 1
        for item in resp['Items']:
            print(item)

    else:
        print("over")
        break
