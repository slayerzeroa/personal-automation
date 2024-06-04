from appium import webdriver
from selenium.webdriver.common.options import ArgOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
import datetime
from .tools import *



def start_today_home():
    # 드라이버 생성
    driver = get_driver()

    # 실행 원하는 앱 패키지명
    package_name = "net.bucketplace"

    go_to_app(driver, package_name)
    time.sleep(20)

    click_content_desc(driver, "닫기")
    time.sleep(10)

    click_text(driver, "행운출첵")
    time.sleep(10)

    scroll_and_click_element_by_text(driver, "출석하기")
    time.sleep(10)

    # 앱 종료
    close_app(driver, package_name)
    time.sleep(5)
