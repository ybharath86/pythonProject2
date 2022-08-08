from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import requests as requests

serv_obj=Service("C:\Program Files\chromedriver_win32 (1)\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
alllinks=driver.find_elements(By.XPATH,"//a")
print(len(alllinks))
count=0
for link in alllinks:
    url=link.get_attribute('href')
    try:
        res=requests.head(url)
    except:
        None
    if res.status_code>=400:
        print(url,"broken link")
        count+=1
    else:
        print(url,"valid link")
print('total no of brokenlinks:',count)
