import boto3
from boto3.dynamodb.conditions import Key
import time

dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
table = dynamodb.Table('cbw-test-table')

def deletedata(id):
    startid = id + 1
    endid = startid - 200

    for i in range(endid,startid):
        userid = "a" + str(i)
        resp = table.delete_item(Key={'user-id': userid})
        print("已删除：",userid)


def times(a):
    times=a+1
    id = 100000
    for i in range(1,times):
        start_time = time.time()
        deletedata(id)
        end_time = time.time()
        time_difference = end_time - start_time
        id -= 200
        print('%.3f秒'%time_difference)

if __name__ == '__main__':
    a = 100
    times(a)

