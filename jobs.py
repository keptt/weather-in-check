from apscheduler.schedulers.blocking import BlockingScheduler
from app import main
import default

sched = BlockingScheduler()

@sched.scheduled_job('cron', day_of_week='mon-fri, sun', hour='18', timezone=default.TIMEZONE_STR)
def query_weather():
    main()

sched.start()

