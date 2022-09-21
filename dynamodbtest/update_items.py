import boto3
import time 
dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = dynamodb.Table('cbw-test-table')


for i in range(79901,80000):
    start_time = time.time()
    new_money = 8888
    userid = 'a'+str(i)
    resp = table.update_item(
        Key={"user-id": userid},
        ExpressionAttributeNames={
            "#money": "Money",
        },
        ExpressionAttributeValues={
            ":id": new_money,
        },
        UpdateExpression="SET #money = :id",
    )

    
    end_time = time.time()
    time_difference = end_time - start_time
    print('%.3f秒'%time_difference)
    print('已更新：%s'%userid)
