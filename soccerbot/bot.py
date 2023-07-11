from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get('link') #paste your google forms link here

wait = WebDriverWait(driver, 5)

first_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
first_name.send_keys('First Name')

last_name = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')))
last_name.send_keys('Last Name')

phone_num = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')))
phone_num.send_keys('Phone Number')

submit = wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div/div[2]/form/div[2]/div/div[3]/div[1]/div[1]/div/span/span')))
submit.click()

driver.quit()
