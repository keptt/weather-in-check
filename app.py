import datetime
import pyowm
import pickle
import smtplib
import os

import default
import send_mail as sm


def main():
    owm = pyowm.OWM(default.TOKEN)

    current_date = datetime.date.today()
    tommorow_date = current_date + datetime.timedelta(days=1)

    fc = owm.three_hours_forecast_at_coords(default.COORD_X, default.COORD_Y)
    f = fc.get_forecast()                                                       #return list of weather objects that contain weather info mapped with the time of the day when such weathter is to be expected

    med: float = 0
    count: int = 0

    todays_temprature: int = 0
    tommorows_temperature: int = 0

    detailed_report: str = ''

    for weather in f:                                                                   
        date_of_forecast = weather.get_reference_time('date')                                                       # receive date from weather object

        if date_of_forecast.hour > 6 and date_of_forecast.hour < 21 and date_of_forecast.date() == tommorow_date:   # considering only temperature data from 6 in the morning til 21 o'clock
        
            count += 1
            detailed_report += (' '.join([str(weather.get_reference_time('iso')), str(weather.get_status()), str(weather.get_temperature(unit='celsius')), '\n']))  # form report to later send via male.
                                                                                                                                                                    # contaiins time : status (e g rain, clear, snow...) and tempareture in celcius
            med += weather.get_temperature(unit='celsius')['temp']

    try:
        with open(default.PICKLE_FILE, 'rb') as pickle_handle:
            try:
                todays_temprature = pickle.load(pickle_handle)                                                                              # get todays temperature from pickle. Later we will save tommorows temperature 
                                                                                                                                            # to pickle and tommorow load this "tommorow" temperature as "today"
            except EOFError:                                                                                                                # if file was empty
                todays_temprature = 0
    except FileNotFoundError:
            pass
    with open(default.PICKLE_FILE, 'bw') as pickle_handle: 
        tommorows_temperature = med/count
        pickle.dump(med/count, pickle_handle)

    # if abs(tommorows_temperature - todays_temprature) > (todays_temprature/100)*15:                                                     # difference in more than 15%//4 degrees
    subject = f'Subject: TEMP DIFF {todays_temprature} vs {tommorows_temperature}'
    message = f'Tommorow\'s weather:\n{detailed_report}'
    sm.send_mail(login=default.SMTP_SEND_FROM, password=default.SMTP_PASSWORD, send_to=[default.SMTP_SEND_TO], subject=subject, message=message)
