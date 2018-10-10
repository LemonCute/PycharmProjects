import  requests
from  selenium import webdriver

from selenium.webdriver.chrome.options import Options
def file(text):
    fr=open("file.html","a+",encoding='utf-8')
    fr.write(text)
    fr.close()
def test1():
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-gpu')
    driver = webdriver.Chrome( chrome_options=chrome_options)  #executable_path='./chromedriver',
    driver.get("http://www.zhihu.com")
    print(driver.page_source)
    res=requests.get("https://www.zhihu.com")
    print(res.text)
    driver.close()


def urllib1():
    import urllib.request
    import urllib.parse
    data=bytes(urllib.parse.urlencode({'word':'hello'}),encoding='utf8')
    res1=urllib.request.urlopen("http://httpbin.org/post",data=data)
    # res=urllib.request.urlopen('http://www.baidu.com').read().decode('utf-8')#type:str
    # file(res.replace("\r\n",""))
    print(res1.read())
def urllib2():
    import socket
    import urllib.request
    import urllib.error
    try:
        res1 = urllib.request.urlopen("http://baidu.com",timeout=0.01 )
        print(res1.read())
    except urllib.error.URLError as e :
        if isinstance(e.reason,socket.timeout):
            print("TIME OT")
        #else:print(e)
if __name__=='__main__':
    # test1()
    urllib2()














