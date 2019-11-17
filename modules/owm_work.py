import pyowm
import datetime

def get_tomorrows_avg_temp(owm: pyowm.OWM, coord_x: float, coord_y: float, from_hour24: float=6.0, to_hour24: float=21.0)->list:
    """
    
    Arguments:
        owm {[type]} -- [description]
    
    Keyword Arguments:
        report {bool} -- [description] (default: {True})
    
    Returns:
        [type] -- [description]
    """    
    # med: float = 0
    # count: int = 0
    detailed_report: list = []

    current_date = datetime.date.today()
    tommorow_date = current_date + datetime.timedelta(days=1)

    fc = owm.three_hours_forecast_at_coords(coord_x, coord_y)
    f = fc.get_forecast()                                                       #return list of weather objects that contain weather info mapped with the time of the day when such weathter is to be expected

    for weather in f:                                                           
        date_of_forecast = weather.get_reference_time('date')                                                       # receive date from weather object
        if date_of_forecast.hour > from_hour24 and date_of_forecast.hour < to_hour24 and date_of_forecast.date() == tommorow_date:   # considering only temperature data from 6 in the morning til 21 o'clock
            detailed_report.append([weather.get_reference_time('iso'), weather.get_status(), weather.get_temperature(unit='celsius')])  # form report to later send via male.
            
                                                                                                                                                                    # contaiins time : status (e g rain, clear, snow...) and tempareture in celcius
            # med += weather.get_temperature(unit='celsius')['temp'] 

    return detailed_report
