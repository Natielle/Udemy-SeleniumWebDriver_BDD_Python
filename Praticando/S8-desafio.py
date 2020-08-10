from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time

driver = webdriver.Chrome()
url = "http://www.cfnews.net/user/login"
driver.get(url)

wait = WebDriverWait(driver, 10)
login_form = wait.until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "input#nom-user")), "pbm")

displayed = login_form.is_displayed()
print("login_form.is_displayed() = ", str(displayed))
login_form.send_keys("teste123")
time.sleep(5)

driver.close()