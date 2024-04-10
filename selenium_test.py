import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

# TEST 1: Initial Page
driver.get("http://127.0.0.1:8000/")
time.sleep(0.25)
driver.save_screenshot("./screenshot-1.png")

# TEST 2: Search Jobs
driver.find_element(by=By.CSS_SELECTOR, value="#search").send_keys("Python")
driver.find_element(by=By.CSS_SELECTOR, value="#button-search").click()
time.sleep(0.25)
driver.save_screenshot("./screenshot-2.png") # Expected: Jobs with Python keyword

# TEST 3: Go to Companies Page
driver.find_element(by=By.CSS_SELECTOR, value='a[href="/companies"]').click()
time.sleep(0.25)
driver.save_screenshot("./screenshot-3.png") # Expected: Companies Page

# TEST 4: Search Companies
driver.find_element(by=By.CSS_SELECTOR, value="#search").send_keys("Netflix")
driver.find_element(by=By.CSS_SELECTOR, value="#button-search").click()
time.sleep(0.25)
driver.save_screenshot("./screenshot-4.png") # Expected: Companies with Netflix keyword

# TEST 5: Go to Company Details Page
driver.find_element(by=By.CSS_SELECTOR, value='a[href="/companies/netflix"]').click()
time.sleep(0.25)
driver.save_screenshot("./screenshot-5.png") # Expected: Company Details Page

# TEST 6: See Related Jobs
driver.execute_script("document.querySelector('.jobpost--item').scrollIntoView()")
time.sleep(0.25)
driver.save_screenshot("./screenshot-6.png") # Expected: Related Jobs on Netflix page

driver.quit()