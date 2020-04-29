from selenium import webdriver

Path = "C:\Program Files JN\chromedriver.exe"

driver = webdriver.Chrome(Path)

driver.get("https://techwithtim.net")

print(driver.title)
driver.quit()