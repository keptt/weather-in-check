from apscheduler.schedulers.blocking import BlockingScheduler
from modules import default
import app
# from app import TODAYS_TEMPERATURE

import os

sched = BlockingScheduler()

TODAYS_TEMPERATURE = 0

@sched.scheduled_job('cron',  day_of_week='mon-fri, sun', hour='18', minute='02', timezone=default.TIMEZONE_STR)
def query_weather():
    global TODAYS_TEMPERATURE
    TODAYS_TEMPERATURE = app.main(TODAYS_TEMPERATURE, heroku_mode=True)


if __name__ == '__main__':
    sched.start()
