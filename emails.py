import win32com.client
from twilio.rest import Client

outlook=win32com.client.Dispatch("Outlook.Application")
outlook_ns=outlook.GetNamespace("MAPI")

myfolder=outlook_ns.Folders['james_allen2@baylor.edu'].Folders['Inbox']

messages=myfolder.Items

messagecount=0

for message in messages:
    if message.UnRead:
        #print(message.sender)
        print(message.subject)
        messagecount+=1
"""
        if 'absence' in message.subject: 
            print("Found messge with absence")

            Msg = outlook.CreateItem(0)
            Msg.Importance=1
            Msg.Subject='got your ' + message.subject + ' email'
            Msg. HTMLBody = 'Hi' + str(message.sender) + "\n, sorry you are not well"

            Msg.To= message.sender.GetExchangeUser().PrimarySmtpAddress
            Msg.ReadReceiptRequested=True

            Msg.Send()

            """

accountSID= 'ACe302743d03ac9fd7a5f50b123efb51d8'

authToken='3433b835a45c878e07348cab886b11f5'

Client=Client(accountSID,authToken)

TwilioNumber='+14706836018'

mycellphone='+18172338016'

textmessage=Client.messages.create(to=mycellphone,from_=TwilioNumber,body=messagecount)


print(textmessage.status)

            #figure out how to check how many unread messges there are
