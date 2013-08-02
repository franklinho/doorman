from flask import Flask
import twilio.twiml
from twilio.rest import TwilioRestClient
import time
from datetime import date
from datetime import datetime

app = Flask(__name__)

today = date.today()
time = datetime.now()

account_sid = "AC116da2960e8e2120d89409507cd555e5"
auth_token = "8664d21d23611faec617fab3373d7cd3"
client = TwilioRestClient(account_sid, auth_token)


@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
	if date.weekday(today) <5 and (time.hour > 16 or time.hour <4):

		"""Respond to incoming requests."""
		resp = twilio.twiml.Response()
		resp.say("Welcome to MoPub")
		resp.play("https://googledrive.com/host/0B0URKjV-4_aiUF9SZjlRRmk4RWM/6.mp3")

		message = client.sms.messages.create(to="+14154639857",from_="+14695183938",body="There is someone at the door")
		
		return str(resp)
	else:
		resp = twilio.twiml.Response()
		resp.say("Sorry, MoPub is closed at this time. Please come back between the hours of 9 AM and 6 PM, Monday through Friday")

if __name__ == "__main__":
	app.run(host='0.0.0.0')