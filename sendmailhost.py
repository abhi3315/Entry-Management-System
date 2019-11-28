def send_mail_host(host_mail,a,b,c,d):
    import smtplib
    connection = smtplib.SMTP('smtp.gmail.com' , 587)
    connection.ehlo()
    connection.starttls()
    connection.login('mtesting234@gmail.com' , 'Asinolas')
    msg="Subject: Visitor-Details \n\n Visitor Name: %s \n Checkin Time: %s \n Visitor Mobile: %s \n Visitor Email: %s"%(a,b,c,d)
    connection.sendmail('mtesting234@gmail.com' , host_mail , msg)
    connection.quit()
