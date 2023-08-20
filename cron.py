import schedule
import time
import os

command = "python manage.py crawl"
schedule.every().day.at("00:00").do(lambda: os.system(command))

while True:
    schedule.run_pending()
    time.sleep(1)
