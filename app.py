import datetime
import pyowm
import os
import traceback
from statistics import mean
from pprint import pformat

from modules import default
from modules import send_mail
from modules import owm_work


def main():
    """
    """    
    todays_temperature: int = 0
    tommorows_temperature: int = 0
    subject_error: str = ''
    error_text:str = ''

    owm = pyowm.OWM(default.TOKEN)
    detailed_report = owm_work.get_tomorrows_avg_temp(owm, default.COORD_X, default.COORD_Y)
    tommorows_temperature = mean([row[len(row)-1]['temp'] for row in detailed_report])                                                         # calculates avg temp for tommorow
    detailed_report = pformat(detailed_report)


    todays_temperature = owm_work.get_todays_avg_temp(owm, default.COORD_X, default.COORD_Y)

    # if abs(tommorows_temperature - todays_temprature) > (todays_temprature/100)*15:                                                     # difference in more than 15%//4 degrees
    subject = f'Subject: TEMP DIFF {todays_temperature} vs {tommorows_temperature}' + subject_error
    message = subject_error + f'Tommorow\'s weather:\n{detailed_report}\n' + error_text 
    send_mail.send_mail(login=default.SMTP_SEND_FROM, password=default.SMTP_PASSWORD, send_to=[default.SMTP_SEND_TO], subject=subject, message=message)


if __name__ == '__main__':
    main()
