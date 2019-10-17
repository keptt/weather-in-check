from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
import default

import send_mail as sm
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri, sun', hour='18', minute='05', timezone=default.TIMEZONE_STR)
def query_weather():
    main()

sched.start()
