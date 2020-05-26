from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "C:\Program Files JN\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://accounts.google.com/signin/v2/identifier?service=mail&passive=true&rm=false&continue=https%3A%2F%2Fmail.google.com%2Fmail%2F&ss=1&scc=1&ltmpl=default&ltmplcache=2&emr=1&osid=1&flowName=GlifWebSignIn&flowEntry=ServiceLogin")

MyUserName = 
MyPassword = 

emailElem = driver.find_element_by_name('identifier')
emailElem.send_keys(MyUserName)
nextButton = driver.find_element_by_id('identifierNext')
nextButton.click()
time.sleep(1)
passwordElem = driver.find_element_by_id('Passwd')
passwordElem.send_keys(MyPassword)
signinButton = driver.find_element_by_id('signIn')
signinButton.click()
