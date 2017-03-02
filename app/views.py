from flask import render_template
from app import app
import urllib.request
import json
import datetime
from .helper import *

@app.route('/')
@app.route('/index')

def index():
	city = 'Austin'
	state = 'TX'
	today = datetime.datetime.now()

	conditionsURL = createConditionsURL(city, state)
	conditionsData = createData(conditionsURL)

	forecastURL = createForecastURL(city, state)
	forecastData = createData(forecastURL)

	degree_sign= u'\N{DEGREE SIGN}'
	temperature = str(conditionsData['current_observation']['temp_f']) + str(degree_sign)
	precipitation = str(forecastData['forecast']['txt_forecast']['forecastday'][0]['pop']) + '%'
	weather = str(conditionsData['current_observation']['weather']).lower()

	if int(today.strftime("%H")) >= 19 and int(today.strftime("%H")) < 4:
		greeting = 'Good Night'
	elif int(today.strftime("%H")) >= 4 and int(today.strftime("%H")) <= 12:
		greeting = 'Good Morning'
	else:
		greeting = 'Good Afternoon'

	if 'rain' in weather:
		symbol = str(u'\u26C6')
	elif 'cloud' in weather and 'part' in weather:
		symbol = str(u'\u26C5')
	elif 'cloud' in weather:
		symbol = str(u'\u2601')
	elif 'storm' in weather:
		symcol = str(u'\u26A1')
	else:
		symbol = str(u'\u2600')		

	user = {'nickname': 'Megan'}
	currentDate = today.strftime("%A %B %d, %Y")
	currentTime = today.strftime("%I:%M %p")
	return render_template('index.html', user=user, currentDate=currentDate, currentTime=currentTime, temperature=temperature, city=city, state=state, precipitation=precipitation, greeting=greeting, symbol=symbol)




