import pymysql
import re
def retime(file):

    fr=open(file=file,mode="r+",encoding="utf-8")
    content=fr.read()
    # print(content)
    mat = re.findall(r'<a href="(.*?)" target="_blank"\s*title=.*?>(.*?)</a>', content)
    print(mat)
    return  mat

def filew(mode,content:str):
    fr = open(file="result.txt", mode=mode, encoding="utf-8")
    fr.write(content)
    fr.close()


def insql(mat):
    conn = pymysql.Connect(
        host='localhost',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='root',##用户名
        passwd='',##密码
        db='pybase',##数据库名
        charset='utf8mb4'
    )
    cursor = conn.cursor()
    for item in mat:
        count = cursor.execute("insert into music(url,name) values(%s,%s)",item)
        conn.commit()

    cursor.close()
    conn.close()

def insql1():
    try:
        conn =  pymysql.Connect(
        host='localhost',##mysql服务器地址
        port=3306,##mysql服务器端口号
        user='root',##用户名
        passwd='',##密码
        db='pybase'##数据库名
        )
        cs1 = conn.cursor()
        sname = input('请输入学生姓名：')
        gender = input('请输入学生性别：')

        count = cs1.execute("insert into music(url,name) values(%s,%s)"%(sname,gender))
        print(count)
        conn.commit()
        cs1.close()
        conn.close()

    except Exception as e:
        print(e.message)


if __name__=="__main__":
    mat=retime("file.html")
    insql(mat)
    #insql1()
    # for item in mat:
        # print(item[1],item[0])
        # content=",".join(item)
        # filew("a",content+",\n")