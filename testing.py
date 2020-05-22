from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

Path = "C:\Program Files JN\chromedriver.exe"
driver = webdriver.Chrome(Path)

driver.get("https://www.amazon.co.uk/") #load site#

time.sleep(3)

search = driver.find_element_by_name("field-keywords")
search.send_keys("speaker")
search.send_keys(Keys.RETURN)