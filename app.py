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

    fc = owm.three_hours_forecast_at_coords()
    f = fc.get_forecast(default.COORD_X, default.COORD_Y)

    #print(type(tommorow_weather.get_reference_time('date')), tommorow_weather.get_status(), tommorow_weather.get_temperature(unit='celsius'))

    med: float = 0
    count: int = 0

    todays_temprature: int = 0
    tommorows_temperature: int = 0

    detailed_report: str = ''

    for weather in f:
        date_of_forecast = weather.get_reference_time('date')

        # print('tommorow:')
        if date_of_forecast.hour > 6 and date_of_forecast.hour < 21 and date_of_forecast.date() == tommorow_date:
            # print(weather.get_reference_time('iso'), weather.get_status(), weather.get_temperature(unit='celsius'))
        
            count += 1
            detailed_report += (' '.join([str(weather.get_reference_time('iso')), str(weather.get_status()), str(weather.get_temperature(unit='celsius')), '\n']))
            med += weather.get_temperature(unit='celsius')['temp']


    if  os.path.exists(os.path.join(os.getcwd(), default.PICKLE_FILE)):  
        with open(default.PICKLE_FILE, 'rb') as pickle_handle:
            todays_temprature = pickle.load(pickle_handle)
        with open(default.PICKLE_FILE, 'bw') as pickle_handle: 
            tommorows_temperature = med/count
            pickle.dump(med/count, pickle_handle)
        

    # print(f'{tommorows_temperature} vs {todays_temprature}  diff = {tommorows_temperature - todays_temprature} 15% = {(todays_temprature/100)*20}')

    if abs(tommorows_temperature - todays_temprature) > (todays_temprature/100)*15:                                                     #difference in more than 20%//4 degrees
        subject = f'Subject: TEMP DIFF {todays_temprature} vs {tommorows_temperature}'
        message = f'{detailed_report}'
        sm.send_mail(login=default.SMTP_SEND_FROM, password=defaults.SMTP_PASSWORD, send_to=default.SMTP_SEND_TO, subject=subject, message=message)
