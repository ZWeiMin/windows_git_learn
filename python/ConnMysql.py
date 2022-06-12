# pylint: disable=no-member
import pymysql
connection = pymysql.connect(host='localhost',user='root',password='123456',charset='utf8',db='datatest')
cursor=connection.cursor()#游标
sql='select * from student1'
cursor.execute(sql)
result=cursor.fetchall()
for row in result:
    print(row)
connection.close()
cursor.close()
