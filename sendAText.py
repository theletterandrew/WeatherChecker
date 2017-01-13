# sendAText.py - Defines SendText(), a function that sends a given recipient a message passed as a string.

accountSID = ''
authToken = ''
twilioNumber = ''
svcID = ''

from twilio.rest import TwilioRestClient

def SendText(message, recipient):
	twilioCli = TwilioRestClient(accountSID, authToken)
	twilioCli.messages.create(body=message, from_=twilioNumber, to=recipient)