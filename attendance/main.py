from app.appium import music_cow
from app.appium import ok_cashback
from app.appium import today_home
from app.appium import tools

import time
import datetime


while True:
    ## 매일 00시 01분에 실행
    now = datetime.datetime.now()
    if now.hour == 0 and now.minute == 1:
        try:
            # today_home.start_today_home()
            music_cow.start_music_cow()
            ok_cashback.start_ok_cashback()
        except Exception as e:
            print(f"An error occurred: {e}")