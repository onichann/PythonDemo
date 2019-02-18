import pymysql


def insert(table, data):
    data = {
        'id': '12312312',
        'name': 'bob',
        'age': 20
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    sql = 'insert into {table}({keys}) values({values})'.format(table=table, keys=keys, values=values)
    try:
        db = pymysql.Connect(host='127.0.0.1', user='root', password='root', port=3306, db='pydb')
        cursor = db.cursor()
        if cursor.execute(sql, tuple(data.values())):
            print('successful')
            db.commit()
    except Exception as e:
        print('failed')
        db.rollback()
    db.close()


if __name__ == '__main__':
    data = {
        'id': '12312312',
        'name': 'bob',
        'age': 20
    }
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    print(keys)
    print(values)
