import boto3
import random
import time

def insert(id):
    dynamodb = boto3.resource('dynamodb', region_name='ap-northeast-1')
    table = dynamodb.Table('cbw-test-table')
    idstart = id
    idend = idstart + 25
    with table.batch_writer() as batch:
        for i in range(idstart,idend):
            Userid="a"+str(i)
            Servid="a"+str(random.randint(1,10000))
            Power=random.randint(1,100000)
            Charm=random.randint(1,100000)
            Money=random.randint(1,100000)
            Intimacy=random.randint(1,100000)
            batch.put_item(Item={"user-id": Userid, "server-id": Servid,"Power": Power, "Charm": Charm, "Money": Money, "Intimacy": Intimacy })
            print(Userid)
            continue

def times(a):
    times=a+1
    id = 100026
    for i in range(1,times):
        start_time = time.time()
        insert(id)
        end_time = time.time()
        time_difference = end_time - start_time
        id += 25
        print('%.3f秒'%time_difference)


if __name__ == '__main__':
    a = 100
    times(a)

