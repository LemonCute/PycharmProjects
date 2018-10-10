# 建立数据库连接
import pymysql

conn = pymysql.Connect(
    host='localhost',##mysql服务器地址
    port=3306,##mysql服务器端口号
    user='root',##用户名
    passwd='',##密码
    db='threephp'##数据库名

)

sql = """INSERT INTO music(url, name) VALUES (item[0],item[1]) """
cursor.execute(sql)  # 执行sql语句
conn.commit()  # 提交到数据库执行
cursor = conn.cursor()
cursor.execute('SELECT * FROM user')
# sql = "SELECT *FROM login"
# cursor.execute(sql)
cursor = conn.cursor()

conn.close()


# print(cursor.rowcount)
# rr = cursor.fetchall()  # 将所有的结果放入rr中
# # 对结果进行处理
# for row in rr:
#     print("ID是：=%s, 姓名是：=%s, 密码是：=%s" % row)
# # print(re)#输出两条数据，因为fetch()方法是建立在上一次fetch()方法基础上的

