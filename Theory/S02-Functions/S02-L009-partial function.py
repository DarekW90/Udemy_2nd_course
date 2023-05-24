import smtplib
import functools


def SendInfoEmail(user,password,mailFrom,mailTo,mailSubject,mailBody):
    message = '''From: {}
Subject: {}
{}
'''.format(mailFrom, mailSubject, mailBody)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(user,password)
        server.sendmail(user,mailTo,message)
        server.close()
        print('mail sent')
        return True
    except:
        print('error sending email')
        return False


mailFrom = 'Nazwa'
mailTo = ['123@gmail.com', '456@gmail.com']
mailSubject = 'Processing finished successfully'
mailBody = '''Hello!

This mail confirms that processing has finished without problems,

Have a nice Day!'''

user = 'tu_podaj_mail@gmail.com'
password = 'tu_pwd'

SendInfoEmailFromGmail = functools.partial(SendInfoEmail, user, password)

SendInfoEmailFromGmail(mailFrom, mailTo, mailSubject, mailBody)

SendInfoEmail(user, password, mailFrom, mailTo, mailSubject, mailBody)
