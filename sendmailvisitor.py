def send_mail_visitor(visitor_mail,a,b,c,d,e,f):
    import smtplib
    connection = smtplib.SMTP('smtp.gmail.com' , 587)
    connection.ehlo()
    connection.starttls()
    connection.login('mtesting234@gmail.com' , 'Asinolas')
    msg="Subject: Today-Visit \n\n Name: %s \n Phone: %s \n Checkin Time: %s \n Checkout Time: %s \n Address Visited: %s \n Host Name: %s"%(a,b,c,d,e,f)
    connection.sendmail('mtesting234@gmail.com' , visitor_mail , msg)
    connection.quit()
