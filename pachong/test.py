import pymongo as pymongo
import pymysql as pymysql
from  selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pyquery

def main():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    #chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome( chrome_options=chrome_options)  #executable_path='./chromedriver',
    driver.get("https://www.leck.top")
   # print(driver.page_source)
    driver.close()
def demo2():
    pyquery.get()
def mysql2():
    conn = pymysql.Connect(
        host='localhost',  ##mysql服务器地址
        port=3306,  ##mysql服务器端口号
        user='root',  ##用户名
        passwd='',  ##密码
        db='threephp',  ##数据库名
        charset = 'utf8'  ##连接编码
    )
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM user')
    # print(cursor.rowcount)#查询到的信息条数
    # rs=cursor.fetchone()#将第一条结果放入rs中
    # re=cursor.fetchmany(3)#将多个结果放入re中
    rr = cursor.fetchall()  # 将所有的结果放入rr中
    # 对结果进行处理
    for row in rr:  #for(int i;i<rr.length;i++)
        # print(row)# for i in row:#         #     print(i)
        print(row)
def mongo():
    client=pymongo.MongoClient('localhost')
    db=client['lemondb']
    data = {'id': 123, 'name': 'Neil', 'age': 80, 'sex': 'male'}
    db['table'].insert(data)
    # db['table'].find_one(())

if __name__ == '__main__':
    main()