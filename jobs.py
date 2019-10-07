from apscheduler.schedulers.blocking import BlockingScheduler
from send_mail import main
import default

sched = BlockingScheduler()

@sched.scheduled_job('cron', days_of_week='sun-fri', hour='18', timezone=default.TIMEZONE_STR)
def query_weather():
    main()
