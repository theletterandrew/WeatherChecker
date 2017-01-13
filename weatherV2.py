# weatherV2.py
# Version 2 of the Inclement Weather Notification program
# The major change from the first version is the ability to add other people to my 'contact list'
# I'm also trying to implement an OOP design to the code

import json, requests, sendAnEmail, sendAText

class User(object):
	def __init__(self, name, phone, locations, lowTemp):
		self.name = name
		self.phone = phone
		self.locations = locations
		self.lowTemp = lowTemp


	def checkWeather(self):
		rain = []
		cold = []
		
		for item in self.locations:
			address = 'http://api.wunderground.com/api/' + '**YOUR-API-KEY**' + '/forecast/q/'+ '**YOUR-STATE**' + '/' + item + '.json'
			response = requests.get(address)
			response.raise_for_status()
			weather = json.loads(response.text)
			POP = weather['forecast']['txt_forecast']['forecastday'][0]['pop']
			low = weather['forecast']['simpleforecast']['forecastday'][0]['low']['fahrenheit']

			if float(POP) >= 20:
				rain.append((item, POP))
			if float(low) <= self.lowTemp:
				cold.append((item, low))

		if rain or cold:
			message = "\n\nHey, " + self.name + "! \n\nJust a friendly reminder to"
			if rain and cold:
				message += " bring both an umbrella and a jacket! \n\nHere's the forecast:\n"
				for item in rain:
					message += item[1] + "% chance of rain in " + item[0] + "\n"
				for item in cold:
					message += item[1] + '\u00b0' + "F in " + item[0] + "\n"
			elif rain:
				message += " bring an umbrella!\n\nHere's the forecast:\n"
				for item in rain:
					message += item[1] + "% chance of rain in " + item[0] + "\n"
			elif cold:
				message += " bring a jacket!\n\nHere's the forecast:\n"
				for item in cold:
					message += item[1] + '\u00b0' + "F in " + item[0] + "\n"

		return message

	def notifyUser(self):
		if self.checkWeather() != None:
			sendAText.SendText(self.checkWeather(), self.phone)