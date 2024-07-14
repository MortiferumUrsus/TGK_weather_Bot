from Telegramm_bot import every_day_post
import schedule
import time

if __name__ == '__main__':
    print("start")
    schedule.every().day.at("17:00").do(every_day_post)
    while True:
        schedule.run_pending()
        time.sleep(1)