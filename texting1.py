from twilio.rest import Client

accountSID= 'ACe302743d03ac9fd7a5f50b123efb51d8'

authToken='3433b835a45c878e07348cab886b11f5'

Client=Client(accountSID,authToken)

TwilioNumber='+14706836018'

mycellphone='+18172338016'

textmessage=Client.messages.create(to=mycellphone,from_=TwilioNumber,body="Hello World!")


print(textmessage.status)



#make a phone call
call=Client.calls.create(url="http://demo.twiliio.com/docs/voice.xml",to=mycellphone, from_=TwilioNumber)