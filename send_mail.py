import smtplib
from email.mime.text import MIMEText

def send_mail(login, password, send_to, subject, message, service='smtp.gmail.com', port=587):
    prepared_message = MIMEText(message)
    prepared_message['From'] = login
    prepared_message['To'] = ', '.join(send_to)
    prepared_message['Subject'] = subject
    
    smtp_obj = smtplib.SMTP(service, port)
    smtp_obj.starttls()
    smtp_obj.login(login, password)
    smtp_obj.sendmail(login, send_to, prepared_message.as_string())
    smtp_obj.quit()
