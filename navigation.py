from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "C:\Program Files JN\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://techwithtim.net")

    #find + click beginner python programming# 
link = driver.find_element_by_link_text("Python Programming")
link.click()

    #find + click beginner python tutorials link#  
try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beginner Python Tutorials"))
    )
    element.click()

    #find + click get started button#
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "sow-button-19310003"))
    )
    element.click()

    driver.back()
    driver.back()
    driver.back()
    print("done!")
except:
    driver.quit()


