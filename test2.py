from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import os
location = os.getcwd()

serv_obj=Service("C:\Program Files\chromedriver_win32 (1)\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
opt=webdriver.ChromeOptions()
preference={"download.default_directory":location}
opt.add_experimental_option("prefs",preference)
# driver.find_element(By.XPATH,"//textarea[@id='textbox']").send_keys('heloooooooooooooo')
# driver.find_element(By.XPATH,"//button[@id='createTxt']").click()
# driver.find_element(By.XPATH,"//a[@id='link-to-download']").click()

driver.find_element(By.XPATH,"//textarea[@id='pdfbox']").send_keys('heloooooooooooooo')
driver.find_element(By.XPATH,"//button[@id='createPdf']").click()
driver.find_element(By.XPATH,"//a[@id='pdf-link-to-download']").click()