import datetime
import pyowm
import os
import traceback
from statistics import mean
from pprint import pformat

from modules import default
from modules import send_mail
from modules import pickle_routine
from modules import owm_work


def main(in_todays_temperature=0, heroku_mode: bool=False):
    """
    Keyword Arguments:
        heroku_mode {bool} -- [description] (default: {False})
    """    
    todays_temperature: int = 0
    tommorows_temperature: int = 0
    subject_error: str = ''
    error_text:str = ''

    owm = pyowm.OWM(default.TOKEN)
    detailed_report = owm_work.get_tomorrows_avg_temp(owm, default.COORD_X, default.COORD_Y)
    tommorows_temperature = mean([row[len(row)-1]['temp'] for row in detailed_report])                                                         # calculates avg temp for tommorow
    detailed_report = pformat(detailed_report)

    if heroku_mode:
        todays_temperature = in_todays_temperature
        in_todays_temperature = tommorows_temperature
    else:
        try:
            todays_temperature = pickle_routine.pickle_get(default.PICKLE_FILE)                                                                                # get todays temperature from pickle. Later we will save tommorows temperature 
                                                                                                                                                # to pickle and tommorow load this "tommorow" temperature as "today"                                                                                          
        except EOFError:                                                                                                                        # if file wasn't found empty                                                                                           
            pass
        except FileNotFoundError:
            subject_error = f' File {default.PICKLE_FILE} not found on filesystem|'
        except:
            subject_error += f'| Pickle get {default.PICKLE_FILE} issue|'
            error_text = f'ERROR desc:\n{traceback.format_exc()}'
        try:
            pickle_routine.pickle_put(default.PICKLE_FILE, tommorows_temperature)
        except:
            subject_error += f'| Put to {default.PICKLE_FILE} issue|'
            error_text = f'ERROR desc:\n{traceback.format_exc()}'

    # if abs(tommorows_temperature - todays_temprature) > (todays_temprature/100)*15:                                                     # difference in more than 15%//4 degrees
    subject = f'Subject: TEMP DIFF {todays_temperature} vs {tommorows_temperature}' + subject_error
    message = subject_error + f'Tommorow\'s weather:\n{detailed_report}\n' + error_text 
    send_mail.send_mail(login=default.SMTP_SEND_FROM, password=default.SMTP_PASSWORD, send_to=[default.SMTP_SEND_TO], subject=subject, message=message)

    return in_todays_temperature

if __name__ == '__main__':
    main()
