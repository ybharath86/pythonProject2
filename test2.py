# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # # import os
# # #
# # #
# # # serv_obj =Service("")
# # # driver=webdriver.Chrome(service=serv_obj)
# # # driver.get("https://opensource-demo.orangehrmlive.com/")
# # # driver.maximize_window()
# # # driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
# # # driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys('admin123')
# # # driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
# # # driver.save_screenshot(os.getcwd()+"\\orangehrmlogin.png")
# # #
# #
# # #headless mode
# # # from selenium import webdriver
# # # def headless_chrome():
# # #     from selenium.webdriver.chrome.service import Service
# # #     serv_obj=Service("C:\Program Files\chromedriver_win32\chromedriver")
# # #     ops = webdriver.ChromeOptions()
# # #     ops.headless = True
# # #     driver= webdriver.Chrome(service=serv_obj)
# # #     return driver
# # # driver = headless_chrome()
# # # driver.get("//opensource-demo.orangehrmlive.com/")
# # # print(driver.title)
# # # driver.close()
# # #
# # from selenium import webdriver
# # from selenium.webdriver.common.by import By
# # # import os
# # # location=os.getcwd()
# # # def Chrome_setup():
# # #     from selenium.webdriver.chrome.service import Service
# # #     serv_obj=Service("C:\Program Files\chromedriver_win32\chromedriver")
# # #     preference={'download.default_directory':location}
# # #     ops=webdriver.ChromeOptions()
# # #     ops.add_experimental_option('prefs',preference)
# # #     driver=webdriver.Chrome(service=serv_obj)
# # #     return driver
# # # driver= Chrome_setup()
# # # driver.get("https://opensource-demo.orangehrmlive.com/")
# # # driver.maximize_window()
# # import openpyxl
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# #
# # #file--WORKBOOK--SHEET--ROW--CELL
# # # file=""
# # # workbook=openpyxl.load_workbook(file)
# # # sheet=workbook['sheet1']
# # # rows=sheet.max_row
# # # cols=sheet.max_coll
# # # #read all data from excel
# # # for r in range(2,rows+1):
# # #     for c in range(1,cols+1):
# # #         print(sheet.cell(r,c).value,end=' ')
# # #         print()
# # #
# # #
# # # #write data into excel
# # # file=""
# # # workbook=openpyxl.load_workbook(file)
# # # sheet=workbook['data']
# # # for r in range(1,6):
# # #     for c in range(1,4):
# # #         sheet.cell(r,c).value ='selenium'
# # # workbook.save(file)
# # # from excel import utilies
# # # from selenium import webdriver
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.support.ui import Select
# # # import openpyxl
# # # serv_obj =Service("")
# # # driver=webdriver.Chrome(service=serv_obj)
# # # file=("")
# # #
# # # rows=utilies.getrowcount(file,sheet)
# # # for r in range(2,rows+1):
# # #
# # #     pref=utilies.readdata(file,'sheet',r,1)
# # #     rateofint=utilies.readdata(file,'sheet',r,2)
# # #     per1=utilies.readdata(file,'sheet1',r,3)
# # #     per2=utilies.readdata(file,'sheet1',r,4)
# # #     freq=utilies.readdata(file,'sheet1',r,5)
# # #     exp_value=utilies.readdata(file,'sheet1',r,6)
# # #
# # #     driver.find_element(By.XPATH, "//input[@id='principal']").send_keys(pref)
# # #     driver.find_element(By.XPATH, "//input[@id='interest']").send_keys(rateofintrst)
# # #     driver.find_element(By.XPATH, "//input[@id='tenure']").send_keys(per1)
# # #     perioddrp = Select(driver.find_element(By.XPATH, "//select[@id='tenurePeriod']"))
# # #     perioddrp.select_by_visible_text(per2)
# # #     frequency = Select(driver.find_element(By.XPATH, "//select[@id='frequency']"))
# # #     frequency.select_by_visible_text(fre)
# # #     driver.find_element(By.XPATH, "//*[@id='fdMatVal']/div[2]/a[1]/img").click()
# # #     act_value = driver.find_element(By.XPATH, "//span[@id='resp_matval']/strong").text
# # #
# # #     if float(exp_value) ==float(act_value):
# # #         print('test passed')
# # #         utilies.writedata(file,'sheet1',r,8,'passed')
# # #         utilies.fillgreencolor(file,'sheet1',r,8)
# # #     else:
# # #         print('test failed')
# # #         utilies.writedata(file,'sheet1',r,8,'failed')
# # #         utilies.fillredcolour(file,'sheet1',r,8)
# # #     driver.find_element(By.XPATH,"").click()
# # # driver.close()
# # #
# #
# #
# # # import mysql.connector
# # # try:
# # #     con=mysql.connector.connect(host='localhost',port=3306,username='root',password='root',database='mydb')
# # #     curs=con.cursor()
# # #     curs.execute('insert into student set kim=104')
# # #     con.commit()
# # #     con.close()
# # # except:
# # #     print('unsucessful')
# # # print('finished')
# # # import mysql.connector
# # # try:
# # #     con=mysql.connector.connect(host='ocalhost',port=3306,username='root',password='root',database='mydb')
# # #     curs=con.cursor()
# # #     curs.execute('delete from set mary=104')
# # #     con.commit()
# # #     con.close()
# # # except:
# # #     print('unsucessful')
# # # print('finished')
# # #
# # # import mysql.connector
# # # try:
# # #     con=mysql.connector.connect(host='myhost',port=3306,username='root',password='root',database='mydb')
# # #     curs=con.cursor()
# # #     curs.execute('update data in kim=104')
# # #     con.commit()
# # #     con.close
# # # except:
# # #     print('unsucessful')
# # # print('finished')
# # # import mysql.connector
# # # try:
# # #
# # #     con=mysql.connector.connect(host='localhost',port=3306,username='root',password='root'database='mydb')
# # #     curs=con.cursor()
# # #     curs.execute('insert into the student kim=104')
# # #     con.commit()
# # #     con.close()
# # # except:
# # #     print('unsucessful')
# # # print('finished')
# #
# # # from selenium import webdriver
# # # from selenium.webdriver.common.by import By
# # # from selenium.webdriver.chrome.service import Service
# # # from selenium.webdriver.support.ui import Select
# # # import mysql.connector
# # #
# # # serv_obj=Service("")
# # # driver=webdriver.Chrome(service=serv_obj)
# # # con=mysql.connector.connect(host='localhost',port=3306,username='root',password='root',database='mydb')
# # # curs=con.cursor()
# # # curs.execute('select * from data')
# # #
# # # try:
# # #     for row in curs:
# # #         pref=row[0]
# # #         rateofint=row[1]
# # #         per1=row[2]
# # #         per2=row[3]
# # #         freq=row[4]
# # #         exp_value=row[5]
# # #
# # #         driver.find_element(By.XPATH,"").send_keys(pref)
# # #         driver.find_element(By.XPATH,"").send_keys(rateofint)
# # #         driver.find_element(By.XPATH,"").send_keys(per1)
# # #         drpdown=Select(driver.find_element(By.XPATH,""))
# # #         drpdown.select_by_visible_text(per2)
# # #         dropdwn=Select(driver.find_element(By.XPATH,""))
# # #         dropdwn.select_by_visible_text(freq)
# # #         act_value=driver.find_element(By.XPATH,"").text
# # #
# # #         if float(act_value) == float(exp_value):
# # #             print('test passed')
# # #         else:
# # #             print('failed')
# # #             driver.find_element(By.XPATH,"").click()
# # #         con.close()
# # # except:
# # #     print('unsucessful')
# # # driver.close()
# # #
# #
# #
# #
# # from excel import utilies
# # from selenium import webdriver
# # from selenium.webdriver.chrome.service import Service
# # from selenium.webdriver.common.by import By
# # from selenium.webdriver.support.ui import Select
# # import openpyxl
# # from openpyxl.styles import PatternFill
# #
# # serv_obj=Service("")
# # driver=webdriver.Chrome(service=serv_obj)
# # driver.get("")
# # driver.maximize_window()
# # file=("")
# # noofrows=utilies.getrowcount(file,'data')
# #
# # for r in range(2,noofrows+1):
# #     pref=utilies.readdata(file,'data',r,1)
# #     rateofintst=utilies.readdata(file,'data',r,2)
# #     per1=utilies.readdata(file,'data',r,3)
# #     per2=utilies.readdata(file,'data',r,4)
# #     freq=utilies.readdata(file,'data',r,5)
# #     exp_value=utilies.readdata(file,'data',r,6)
# #
# #     driver.find_element(By.XPATH,"").send_keys(pref)
# #     driver.find_element(By.XPATH,"").send_keys(rateofintst)
# #     driver.find_element(By.XPATH,"").send_keys(per1)
# #     perioddrp=Select(driver.find_element(By.XPATH,""))
# #     perioddrp.select_by_visible_text(per2)
# #     frequencydrp=Select(driver.find_element(By.XPATH,""))
# #     frequencydrp.select_by_visible_text(freq)
# #     actvalue=driver.find_element(By.XPATH,"").text
# #
# #     if float(exp_value) == float(actvalue):
# #         print('test passed')
# #         utilies.writedata(file,'data',r,8,'passed')
# #         utilies.fillgreencolor(file,'data',r,8)
# #     else:
# #         print('test failed')
# #         utilies.writedata(file,'data',r,8,'failed')
# #         utilies.fillredcolour(file,'data',r,8,)
# #     driver.find_element(By.XPATH,"").click()
# # driver.close()
# # import openpyxl
# # file=''
# # workbook=openpyxl.load_workbook(file)
# # sheet=workbook['sheet1']
# # rows=sheet.max_row
# # column=sheet.max_column
# # #read data
# # for r in range(1,rows+1):
# #     for c in range(1,column+1)
# #         print()
# #
# # #write data of same value
# # import openpyxl
# # file=""
# # workbook=openpyxl.load_workbook(file)
# # sheet=workbook['data']
# # for r in range(1,6):
# #     for c in range(1,4):
# #         sheet.cell(r,c).value='selenium'
# # workbook.save(file)
# #
# # #for diff data
# # file=''
# # workbook=openpyxl.load_workbook(file)
# # sheet=workbook['data']
# # sheet.cell(1,1).value='1'
# # sheet.cell(1,2).value='bharath'
# # sheet.cell(1,3).value='engineer'
# #
# # sheet.cell(2,1).value='2'
# # sheet.cell(2,2).value='bharath'
# # sheet.cell(2,3).value='engineer'
# #
# # sheet.cell(3,1).value='3'
# # sheet.cell(3,2).value='bharath'
# # sheet.cell(3,3).value='engineer'
# # workbook.save(file)
# #
# # #read data from file
# # file=""
# # workbook=openpyxl.load_workbook(file)
# # sheet=workbook['sheet1']
# # rows=sheet.max_row
# # columns=sheet.max_column
# #
# # for r in range(1,rows+1):
# #     for c in range(2,columns+1):
# #         print()
# #
# # #write data
# # file=''
# # workbook=openpyxl.load_workbook(file)
# # sheet=workbook['data']
# # #for same data
# # for r in range(1,6):
# #     for c in range(1,4):
# #         sheet.cell(r,c).value='helloo'
# # workbook.save(file)
# # #for dif valu
# # sheet.cell(1,1).value='1'
# # sheet.cell(1,2).value='bahrath'
# # sheet.cell(1,3).value='engineer'
# # workbook.save(file)
# #
# #
# #
# #
# # import mysql.connector
# # con=mysql.connector.connect(host='localhost',port=3306,username='root',password='root',database='mydb')
# # curs=con.cursor()
# # curs.execute('select * from data')
# # try:
# #
# #     for row in curs:
# #         pref=row[0]
# #         rateofintrst=row[1]
# #         perd1=row[2]
# #         perd2=row[3]
# #         freq=row[4]
# #         exp_value=row[5]
# #
# #         driver.find_element(By.XPATH,"").send_keys(pref)
# #         driver.find_element(By.XPATH,'').send_keys(perd1)
# #         predrp=Select(driver.find_element(By.XPATH,""))
# #         predrp.select_by_visible_text(perd2)
# #         fredrp=Select(driver.find_element(By.XPATH,""))
# #         fredrp.select_by_visible_text(fredrp)
# #         act_value=driver.find_element(By.XPATH,"").text
# #
# #         if float(exp_value) == float(act_value):
# #             print('test passed')
# #         else:
# #             print('test failed')
# #         driver.find_element(By.XPATH,"").click()
# #     con.close()
# #
# # except:
# #     print('connection sucessful')
# #
# #
# # driver.close()
# #
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import Select
# from selenium.webdriver.chrome.service import Service
# from selenium.webdriver.common.action_chains import ActionChains
# serv_obj=Service("C:\Program Files\chromedriver_win32 (1)\chromedriver")
# driver=webdriver.Chrome(service=serv_obj)
# driver.get("https://testautomationpractice.blogspot.com/")
# driver.maximize_window()
# print(driver.title)
# print(driver.current_url)
#
# alert=driver.find_element(By.XPATH,"//h2[normalize-space()='Alert']")
# print(alert.is_displayed())
#
# driver.find_element(By.XPATH,"//input[@id='Wikipedia1_wikipedia-search-input']").send_keys('bharath')
# driver.find_element(By.XPATH,"//button[normalize-space()='Click Me']").click()
# driver.switch_to.alert.accept()
# # driver.find_element(By.XPATH,"//input[@id='datepicker']").click()
# # month="April"
# # year='2021'
# # date='1'
# # while True:
# #
# #     mon=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-month']").text
# #     yr=driver.find_element(By.XPATH,"//span[@class='ui-datepicker-year']").text
# #     if month == mon and year ==yr:
# #         break
# #     else:
# #         driver.find_element(By.XPATH,"//span[@class='ui-icon ui-icon-circle-triangle-w']").click()
# #
# # dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
# #
# # for dt in dates:
# #     if dt.text == date:
# #         dt.click()
# #         break
# # speed=Select(driver.find_element(By.XPATH,"//select[@id='speed']"))
# # speed.select_by_visible_text('Slow')
# #
# # files=Select(driver.find_element(By.XPATH,"//select[@id='files']"))
# # files.select_by_visible_text('PDF file')
# #
# # numbers=Select(driver.find_element(By.XPATH,"//select[@id='number']"))
# # numbers.select_by_visible_text('5')
# #
# # product=Select(driver.find_element(By.XPATH,"//select[@id='products']"))
# # product.select_by_visible_text('Yahoo')
# #
# # animal=Select(driver.find_element(By.XPATH,"//select[@id='animals']"))
# # animal.select_by_visible_text('Baby Cat')
# #
# # text=driver.find_element(By.XPATH,"//div[@class='column-left-outer']//div[@class='widget-content']//div[1]")
# # print(text.is_displayed())
#
# noofrows=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr"))
# print(noofrows)
#
# noofcolumn=len(driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr/th"))
# print(noofcolumn)
#
# data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr[7]/td[1]")
# print(data.text)
#
# # for r in range(2,noofrows+1):
# #     for d in range(1,noofcolumn+1):
# #         data=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(d)+"]").text
# #         print(data,end=" ")
# #     print()
# # for r in range(2,noofrows+1):
# #
# #     subjct=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[3]").text
# #     if subjct == "Selenium":
# #         cost=driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td[4]").text
# #         print(subjct,"   ",cost)
# #     print()
# # driver.find_element(By.XPATH,"//input[@id='age']").send_keys('27')
# #
# # code=driver.find_element(By.XPATH,"//div[@id='HTML4']//img")
# # print(code.size)
# # print(code.location)
# #
# # code=driver.find_element(By.XPATH,"//div[@id='HTML12']//img[1]")
# # print(code.size)
# # print(code.location)
# #
# # code=driver.find_element(By.XPATH,"//div[@id='HTML12']//img[1]")
# # print(code.size)
# # print(code.location)
#
#
# #
# # size=driver.find_element(By.XPATH,"//div[@id='resizable']")
# # print(size.size)
# # print(size.location)
# # print(size.text)
# act=ActionChains(driver)
#
# slider=driver.find_element(By.XPATH,"//span[@class='ui-slider-handle ui-corner-all ui-state-default']")
#
# # print(slider.location)
# act.drag_and_drop_by_offset(slider,200,0).perform()
# print(slider.location)
# act=ActionChains(driver)
# source=driver.find_element(By.XPATH,"//img[@alt='the peaks of high tatras']")
# target=driver.find_element(By.XPATH,"//div[@id='trash']")
#
# act.drag_and_drop(source,target).perform()
# act=ActionChains(driver)
# source=driver.find_element(By.XPATH,"//img[@alt='The chalet at the Green mountain lake']")
# target=driver.find_element(By.XPATH,"//div[@id='trash']")
#
# act.drag_and_drop(source,target).perform()
#
#
# act=ActionChains(driver)
# source=driver.find_element(By.XPATH,"//div[@id='draggable']")
# target=driver.find_element(By.XPATH,"//div[@id='droppable']")
#
# act.drag_and_drop(source,target).perform()
#
# text=driver.find_element(By.XPATH,"//input[@id='field1']")
# text.clear()
# text.send_keys('bharath&indu')
# button=driver.find_element(By.XPATH,"//button[normalize-space()='Copy Text']")
# act=ActionChains(driver)
# act.double_click(button).perform()
#
import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys

serv_obj=Service("C:\Program Files\chromedriver_win32 (1)\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("http://www.deadlinkcity.com/")
driver.maximize_window()
import requests as requests




# driver.find_element(By.XPATH,"//span[@id='select2-billing_country-container']").click()
# state=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_country-results']/li")
# print(len(state))
# for st in state:
#     if st.text == "India":
#         st.click()
#         break
#
# driver.find_element(By.XPATH,"//span[@id='select2-billing_state-container']").click()
# country=driver.find_elements(By.XPATH,"//ul[@id='select2-billing_state-results']/li")
# print(len(country))
# for ele in country:
#     if ele.text =="Bihar":
#
#         ele.click()
#         break
# driver.find_element(By.XPATH,"/html/body/div[6]/div[2]/ul[1]/li[4]/a").click()
# driver.close()
#total no of links
# links=driver.find_elements(By.XPATH,"//div[@class='footer-upper']//li/a")
# print(len(links))



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

driver.quit()