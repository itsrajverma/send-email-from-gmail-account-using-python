# import module
import smtplib
# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)
# start TLS for security
s.starttls()
# Authentication
s.login("youremail@gmail.com", "password")
# message to be sent
SUBJECT = "Web authority Subject"
TEXT = "Message body"
message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
# sending the mail
s.sendmail("Web Authority", "sendto@gmail.com", message)
s.quit()