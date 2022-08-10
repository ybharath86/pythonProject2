from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

serv_obj = Service("C:\Program Files\chromedriver_win32\chromedriver")
driver= webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
print(driver.current_url)
print(driver.title)
img=driver.find_element(By.XPATH,"//div[@id='divLogo']//img")
print(img.is_displayed())
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys('admin123')
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
# driver.find_element(By.XPATH,"//*[@id='mainMenuFirstLevelUnorderedList']/li[2]").click()
# noofrows=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr"))
# print(noofrows)
# noofcolumn=len(driver.find_elements(By.XPATH,"//table[@id='resultTable']/tbody/tr/td"))
# print(noofcolumn)
# Count=0
# for r in range(1,noofrows+1):
#
#     subunit=driver.find_element(By.XPATH,"//table[@id='resultTable']/tbody/tr [' +str(r)+ '] /td[7]").text
#     if subunit == 'Development':
#         Count =Count+1
# print('tottal no of rows:',noofrows)
# print('number of development subunit:',Count)
# print('number of other subunit:',(noofrows-Count))
driver.find_element(By.XPATH,"//b[normalize-space()='Leave']").click()
# driver.find_element(By.XPATH,"//a[@id='menu_leave_viewMyLeaveList']").click()
driver.find_element(By.XPATH,"//input[@id='calFromDate']").click()
month =Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
month.select_by_visible_text('Apr')

year=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
year.select_by_visible_text('1994')

dates=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for date in dates:
    if date.text == '1':
        date.click()
        break

driver.find_element(By.XPATH,"//input[@id='calToDate']").click()
mn=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-month']"))
mn.select_by_visible_text('Apr')
yr=Select(driver.find_element(By.XPATH,"//select[@class='ui-datepicker-year']"))
yr.select_by_visible_text('2000')

dts=driver.find_elements(By.XPATH,"//table[@class='ui-datepicker-calendar']/tbody/tr/td/a")
for dt in dts:
    if dt.text == '1':
        dt.click()
        break
canceld=driver.find_element(By.XPATH,"//input[@id='leaveList_chkSearchFilter_0']")
print(canceld.is_enabled())
pending=driver.find_element(By.XPATH,"//input[@id='leaveList_chkSearchFilter_1']")
print(pending.is_selected())
print(pending.is_displayed())
driver.find_element(By.XPATH,"//input[@id='leaveList_txtEmployee_empName']").send_keys("bharath")
subunit=Select(driver.find_element(By.XPATH,"//select[@id='leaveList_cmbSubunit']"))
subunit.select_by_visible_text("Administration")
driver.find_element(By.XPATH,"//input[@id='btnSearch']").click()
# driver.quit()
