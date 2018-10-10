from selenium import webdriver


def scroll(browser):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    browser.execute_script('alert("to buttom")')
    browser.close()
def name(browser):
    input=browser.find_element_by_class_name("title")
    print(input.id,input.location,input.text)

if __name__=="__main__":
    browser =webdriver.Chrome()
    browser.get("http://www.bilibili.com")
    # scroll(browser)
    name(browser)
    print(browser.get_cookies())
    # word=input("按键添加cookies-valuie")
    browser.add_cookie({"name":"lemon","value":word})
    print(browser.get_cookies())
    # browser.implicitly_wait(10)#隐士等待
    input("按键清除cookies")
    browser.delete_all_cookies()
    # print(browser.get_cookies())
    # browser.close()