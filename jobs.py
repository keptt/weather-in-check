from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
import default

import send_mail as sm
import os

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri, sun', hour='18', minute='05', timezone=default.TIMEZONE_STR)
def query_weather():
    main()
#sm.send_mail(login=default.SMTP_SEND_FROM, password=default.SMTP_PASSWORD, send_to=default.SMTP_SEND_TO, subject='adsgtasg', message='1231432')
# @sched.scheduled_job('cron', day_of_week='mon-fri, sun', hour='23', minute='49', timezone=default.TIMEZONE_STR)
# def send():
#     sm.send_mail(login=default.SMTP_SEND_FROM, password=default.SMTP_PASSWORD, send_to=default.SMTP_SEND_TO, subject='adsgtasg', message='1231432')

sched.start()

