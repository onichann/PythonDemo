import pymysql


db=pymysql.Connect(host='127.0.0.1',user='root',password='root',port=3306,db='pydb')
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print('Database version:'+str(data))


sql='insert into students(id,name,age) values(%s,%s,%s)'
try:
    cursor.execute(sql,('111301','xiaoming',12))
    db.commit()
except Exception as e:
    print(e)
    db.rollback()
db.close()
