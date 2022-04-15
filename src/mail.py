import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders


def Send_Mail_Alert():
    fromaddr = "finalyearprojectdemo3@gmail.com"  # sender gmail address
    toaddr = "adnanamjadshaikh@gmail.com"  # reciver gmail address
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alert"
    body = "Drowsy Alert"
    msg.attach(MIMEText(body, 'plain'))
    filename = "alert.png"
    attachment = open("alert.png", "rb")  # image folder

    p = MIMEBase('application', 'octet-stream')
    p.set_payload((attachment).read())

    encoders.encode_base64(p)

    p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
    msg.attach(p)

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls()

    s.login(fromaddr, "kmT&Kvh7UFS9jDgMV4")  # enter sender gmail password here

    text = msg.as_string()

    s.sendmail(fromaddr, toaddr, text)

    s.quit()