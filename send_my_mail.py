import smtplib

from email.mime.text import MIMEText

import datetime

now = datetime.datetime.now()


s = smtplib.SMTP('smtp.gmail.com', 587)

s.starttls()

s.login('mygmail@~~', 'my_app_pwd')

msg = MIMEText('프로그램 끝났다')

msg['Subject'] = '빨리 터미널 확인해라! 현재시각:'+str(now)


s.sendmail("sendmail", "receiver", msg.as_string())

s.quit()
