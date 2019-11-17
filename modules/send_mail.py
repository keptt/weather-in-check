import smtplib, ssl
from email.mime.text import MIMEText

def send_mail(login, password, send_to, subject, message, service='smtp.gmail.com', port=587):
    if isinstance(send_to, str):
        send_to = [send_to]                                  # make a list out if send_to argument if it was passed as a string
    prepared_message = MIMEText(message, 'plain')            # here second argument is optional
    prepared_message['From'] = login
    prepared_message['To'] = ', '.join(send_to)
    prepared_message['Subject'] = subject
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP(service, port) as smtp_obj:
        smtp_obj.starttls(context=context)                  # encrypt your smtp connection
        smtp_obj.login(login, password)
        smtp_obj.sendmail(login, send_to, prepared_message.as_string())
