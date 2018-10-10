from selenium import webdriver

browser=webdriver.Chrome()
browser.get("http://www.bilibli.com")
browser.execute_script("window.open('http://www.bilibli.com')")