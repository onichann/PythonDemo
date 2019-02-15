import pymysql


db=pymysql.Connect(host='127.0.0.1',user='root',password='root',port=3306)
cursor=db.cursor()
cursor.execute('select version()')
data=cursor.fetchone()
print('Database version:'+str(data))
db.close()
