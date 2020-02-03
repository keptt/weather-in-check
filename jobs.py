from apscheduler.schedulers.blocking import BlockingScheduler
from modules import default
import app
# from app import TODAYS_TEMPERATURE

import os

sched = BlockingScheduler()

@sched.scheduled_job('cron',  day_of_week='mon-fri, sun', hour='17', minute='35', timezone=default.TIMEZONE_STR)
def query_weather():
    app.main()


if __name__ == '__main__':
    sched.start()
