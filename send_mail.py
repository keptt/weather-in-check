import smtplib

def send_mail(login, password, send_to, subject, message, service='smtp.gmail.com', port=587):
    smtp_obj = smtplib.SMTP(service, port)
    smtp_obj.ehlo()
    smtp_obj.starttls()
    smtp_obj.login(login, password)
    smtp_obj.sendmail(login, send_to, f'{subject}\n{message}')
    smtp_obj.quit()
