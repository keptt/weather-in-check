import os

TOKEN = os.environ['TOKEN_OWM']
PICKLE_FILE = 'pickle.pp'
SMTP_SERVICE = 'smtp.gmail.com'
SMTP_PORT = 587
SMTP_SEND_FROM = os.environ['AUTOMATA']
SMTP_SEND_TO = os.environ['SEND_TO']
SMTP_PASSWORD = os.environ['PAS_AUTOMATA']
COORD_X = float(os.environ['COORD_X'])
COORD_Y = float(os.environ['COORD_Y'])
TIMEZONE_STR = os.environ['TIMEZONE']
