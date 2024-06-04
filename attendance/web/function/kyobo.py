
import requests
from bs4 import BeautifulSoup as BS
from datetime import date
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

service = Service(executable_path='attendance/selenium/chromedriver.exe')
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
action = ActionChains(driver)

implicit_wait = 10

f = open('attendance/web/env/kyobo.txt', 'r')
id = f.readline().strip()
password = f.readline().strip()
f.close()


# 1. 출석체크 페이지 접속
url = "https://event.kyobobook.co.kr/attendance"
driver.get(url)
driver.implicitly_wait(implicit_wait)

# 2. 로그인 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="welcome_header_wrap"]/div[1]/div/div[2]/ul/li[2]/a').click()
driver.implicitly_wait(implicit_wait)


# 3. 아이디, 비밀번호 입력
driver.find_element(By.XPATH, '//*[@id="mainDiv"]/main/section/div[1]/div[1]/div[1]/div/input').click()
driver.implicitly_wait(implicit_wait)
action.send_keys(id).perform()
driver.implicitly_wait(implicit_wait)
driver.find_element(By.XPATH, '//*[@id="mainDiv"]/main/section/div[1]/div[1]/div[2]/div/input').click()
action.send_keys(password).perform()
driver.implicitly_wait(implicit_wait)
driver.find_element(By.XPATH, '//*[@id="loginBtn"]').click()
time.sleep(30)


# 4. 출석체크 버튼 클릭
driver.find_element(By.XPATH, '//*[@id="contents"]/div/div/div/div[1]/div[1]/button').click()
