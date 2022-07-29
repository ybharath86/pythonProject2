from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import os


serv_obj =Service("C:\Program Files\chromedriver_win32\chromedriver")
driver=webdriver.Chrome(service=serv_obj)
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
driver.find_element(By.XPATH,"//input[@id='txtUsername']").send_keys('admin')
driver.find_element(By.XPATH,"//input[@id='txtPassword']").send_keys('admin123')
driver.find_element(By.XPATH,"//input[@id='btnLogin']").click()
driver.save_screenshot(os.getcwd()+"\\orangehrmlogin.png")
