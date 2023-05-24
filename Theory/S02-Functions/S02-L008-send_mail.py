import smtplib

mailFrom = 'Nazwa'
mailTo = ['123@gmail.com', '456@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello

This mail confirms that processing has finished without problems,

Have a nice Day!'''

message = '''From: {}
Subject: {}

{}

'''.format(mailFrom, mailSubject, mailBody)

user = 'tu_podaj_mail@gmail.com'
password = 'pwd'

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo()
    server.login(user,password)
    server.sendmail(user,mailTo,message)
    server.close()
    print('mail sent')
except:
    print('error sending email')