from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select


Path = "C:\Program Files JN\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://mygs1.gs1uk.org/My-GS1/checkout.ssp?is=login&login=T&origin=customercenter#login-register")

MyUserName = "martin.burrage@cmsdistribution.com"
MyPassword = "Harrogate"

attempt = 0
while attempt < 10:
    try:
        time.sleep(5)
        emailTag = driver.find_element_by_id('login-email')
        emailTag.send_keys(MyUserName)
        break
    except Exception as e:
        print(e)
        attempt = attempt + 1
        pass

time.sleep(1)

passwordTag = driver.find_element_by_name('password')
passwordTag.send_keys(MyPassword)

time.sleep(1)
signinButton = driver.find_element_by_class_name('buttonOrange')
signinButton.click()

time.sleep(10)
Select1 = Select(driver.find_element_by_class_name('numberTypeSelect'))
Select1.select_by_visible_text('GTIN-13')

time.sleep(10)

CompanyPrefixNo = driver.find_element_by_class_name('chosen-search-input')
time.sleep(2)
CompanyPrefixNo.send_keys(5051868)
time.sleep(2)
CompanyPrefixNo.send_keys(Keys.RETURN)

GoToNumberbankBtn = driver.find_element_by_class_name('buttonOrange')
GoToNumberbankBtn.click()

UseNextNumber = Select(driver.find_element_by_class_name('buttonOrange'))
UseNextNumber.click()



print("DONE!!")




