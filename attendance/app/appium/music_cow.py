from appium import webdriver
from selenium.webdriver.common.options import ArgOptions
from appium.webdriver.common.appiumby import AppiumBy
import time
import datetime
# from .tools import *

import tools 

def opening_close_button(driver):
    button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().className("android.widget.Button").clickable(true).enabled(true).index(0)')
    button.click()
    print("Clicked the opening close button.") 


def click_attendance_button(driver):
    try:
        # 특정 버튼 요소를 찾아 클릭
        # 텍스트를 기반으로 요소 찾기
        button = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR,
            'new UiSelector().textContains("출석체크하기").className("android.widget.Button")')
        button.click()
        print("Button clicked successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")



# def start_music_cow():
#     # 드라이버 생성
#     driver = get_driver()

#     # 실행 원하는 앱 패키지명
#     package_name = "com.musicow.android"

#     go_to_app(driver, package_name)
#     time.sleep(10)

#     try:
#         opening_close_button(driver)
#     except:
#         pass

#     click_text(driver, "더보기")
#     time.sleep(10)
#     click_text(driver, "뮤카 포인트")
#     time.sleep(10)

#     # 출석체크 메뉴 들어가기
#     test = find_all_index(driver, 3)
#     test[1].click()
#     time.sleep(10)

#     # 출석체크 버튼 클릭
#     click_attendance_button(driver)
#     time.sleep(20)

#     # 앱 종료
#     close_app(driver, package_name)
#     time.sleep(5)


driver = tools.get_driver()
tools.dump_ui_hierarchy(driver)