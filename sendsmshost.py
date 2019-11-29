def send_sms_host(mobile,a,b,c,d):
    from twilio.rest import Client


    account_sid = 'paste ACCOUNT SID here'
    auth_token = 'paste AUTH TOKEN here'
    client = Client(account_sid, auth_token)
    msg="Subject: Visitor-Details \n\n Visitor Name: %s \n Checkin Time: %s \n Visitor Mobile: %s \n Visitor Email: %s"%(a,b,c,d)

    message = client.messages.create(
             body=msg,
             from_='paste NUMBER here',
             to='+91'+mobile
         )

    print(message.sid)
